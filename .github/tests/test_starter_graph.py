from html import escape
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / '.github/scripts'))
import build_starter_graph as graph


class StarterGraphTest(unittest.TestCase):
    def test_fresh_root_then_user_records(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for path in [graph.TEMPLATE, Path('.github/type-prefixes.json')]:
                target = root / path
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes((ROOT / path).read_bytes())
            with patch.object(graph.library_scan, 'REPO_ROOT', root):
                graph.generate()
                self.assertEqual(self.read_data(root)['nodes'], [])
                for folder, name, content in (
                    ('Projects', 'PROJ-9000-synthetic.md', 'id: PROJ-9000\ntype: project\nlinks: [TICK-9000]'),
                    ('Tickets', 'TICK-9000-synthetic.md', 'id: TICK-9000\ntype: ticket\nlinks: [PROJ-9000, KNOW-9999]'),
                    ('Artifacts', 'ART-9001-synthetic.md', 'id: ART-9001\ntype: artifact\nstored_at: Artifacts/ART-9000-synthetic.txt\nlinks: []'),
                ):
                    target = root / folder / name
                    target.parent.mkdir(exist_ok=True)
                    target.write_text(f'---\n{content}\ntitle: Synthetic classifier\n---\n', encoding='utf-8')
                (root / 'Artifacts/ART-9000-synthetic.txt').write_text('Synthetic payload', encoding='utf-8')
                (root / 'Chats').mkdir()
                (root / 'Chats/2026-01-01.md').write_text(
                    '### CHAT-9000 — Synthetic chat\nLinks: [TICK-9000]\n', encoding='utf-8'
                )
                graph.generate()
                data = self.read_data(root)
                self.assertEqual(len(data['nodes']), 5)
                self.assertEqual(len(data['links']), 2)
                output = (root / graph.OUTPUT).read_text(encoding='utf-8')
                for source_marker in ('Synthetic', 'ART-9000', 'PROJ-9000', 'CHAT-9000', 'KNOW-9999'):
                    self.assertNotIn(source_marker, output)
                if os.environ.get('LIBRARY_CHROMIUM'):
                    self.check_browser(root, output, os.environ['LIBRARY_CHROMIUM'])
                graph.generate()
                self.assertEqual((root / graph.OUTPUT).read_text(encoding='utf-8'), output)

    def read_data(self, root):
        html = (root / graph.OUTPUT).read_text(encoding='utf-8')
        begin = '<script id="library-graph-data" type="application/json">'
        return json.loads(html.split(begin, 1)[1].split('</script>', 1)[0])

    def check_browser(self, root, graph_html, chromium):
        harness = root / 'browser-test.html'
        harness.write_text(
            f'<!doctype html><iframe id="graph" width="412" height="700" srcdoc="{escape(graph_html, quote=True)}"></iframe>'
            + '''<output id="result">WAITING</output><script>
const frame=document.querySelector('#graph'),result=document.querySelector('#result');
const pause=ms=>new Promise(resolve=>setTimeout(resolve,ms));
function lit(canvas){
    const pixels=canvas.getContext('2d').getImageData(0,0,canvas.width,canvas.height).data;
    for(let i=0;i<pixels.length;i+=4) if(pixels[i]>35 || pixels[i+1]>40 || pixels[i+2]>45) return true;
    return false;
}
async function exercise(){
    try {
        const canvas=frame.contentDocument.querySelector('canvas'), win=frame.contentWindow;
        await pause(500);
        if(!canvas || canvas.dataset.nodeCount!=='5' || canvas.dataset.edgeCount!=='2' || !lit(canvas))
            throw Error('Mobile graph failed to render fixture topology');
        canvas.dispatchEvent(new win.WheelEvent('wheel',{deltaY:-160,bubbles:true,cancelable:true}));
        canvas.dispatchEvent(new win.KeyboardEvent('keydown',{key:'ArrowRight',bubbles:true,cancelable:true}));
        frame.width='1024';
        await pause(500);
        if(!lit(canvas)) throw Error('Desktop graph blank after zoom and rotation');
        result.textContent='PASS';
    } catch(error) {result.textContent='FAIL: '+error.message;}
    frame.remove();
}
window.addEventListener('load',exercise,{once:true});
</script>''', encoding='utf-8',
        )
        browser = subprocess.run(
            [chromium, '--headless=new', '--disable-gpu', '--disable-background-networking',
             f'--user-data-dir={root / "browser-profile"}', '--virtual-time-budget=6000',
             '--dump-dom', harness.as_uri()],
            capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=35,
        )
        self.assertEqual(browser.returncode, 0, browser.stderr[-1000:])
        observed = browser.stdout.split('<output id="result">', 1)[-1].split('</output>', 1)[0]
        self.assertEqual(observed, 'PASS')


if __name__ == '__main__':
    unittest.main()

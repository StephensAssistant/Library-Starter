# Library knowledge graph

From the root of your own Library checkout, run `python .github/scripts/build_starter_graph.py`. Open `outputs/library-knowledge-graph.html` in a browser. Run the command again to refresh the graph after adding or linking records.

The HTML works offline. It displays anonymous dots and connections derived from the records in this checkout. An empty Library displays an empty canvas until records are added. Drag or use the arrow keys to rotate, scroll or pinch to zoom, and tap a cluster to focus it. Press Escape to reset.

Keep the generated HTML local unless you intend to share your Library's relationship topology and record counts. The generator includes anonymous node identifiers and explicit links between existing records. The source titles, IDs, paths, and record bodies stay outside the HTML.

To retain a snapshot as a governed Artifact in your own Library, follow [the Artifact creation guide](../Artifacts/_HOW-TO-CREATE.md). Reserve a native and a companion ID, then place a copy of the generated HTML at the native path and use that path as the companion's `stored_at` value.

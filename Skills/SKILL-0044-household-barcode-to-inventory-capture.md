---
id: SKILL-0044
type: skill
title: Household Barcode Product Identification
status: current
created: 2026-09-18
updated: 2026-09-20
owner: Library owner

trigger_phrases: ["scan food barcode", "identify grocery barcode", "barcode product lookup", "barcode inventory batch"]
links: []
tags: [skill, personal-project, household, barcode, open-food-facts]
---

# Household Barcode Product Identification

Identify a packaged household product from an exact barcode and verify the candidate against visible packaging.

## Intent-routing contract

This Skill owns barcode extraction, exact product lookup and package verification. Receipt extraction, attribute enrichment, match auditing and inventory record construction are separate actions.

## When to use

Use for batches of up to five barcode photos or exact GTINs. Do not use for safety-critical allergy decisions.

## Method

1. Number each visible product; process successful items independently.
2. Extract exact EAN, UPC or GTIN digits and validate length and checksum where supported.
3. Never reconstruct, autocomplete or guess unreadable digits.
4. Query the production Open Food Facts product endpoint with the exact barcode and documented read limits.
5. Treat the crowdsourced result as a candidate; preserve absent values as unknown.
6. Verify product name, brand and pack size against visible packaging and ask for one closer image only where required.

## Benchmark case

Four of five barcodes resolve and match visible packaging; the four are returned as verified candidates while only the blurred fifth image is requested again.

## Anti-patterns

- Inferring partial barcode digits
- Treating a database match as automatically correct
- Requiring successful items to be photographed again because one failed
- Copying a database expiry date into a household lot

## Authoritative source

- https://openfoodfacts.github.io/openfoodfacts-server/api/

## Stop

Stop when each barcode is a verified product candidate or has one precise image or identity gap.

## Relationship evidence

RELATIONSHIP-EVIDENCE: PLAY-0061--SKILL-0044 | related_to | undirected | user_confirmed | supports
RELATIONSHIP-EVIDENCE: PLAY-0062--SKILL-0044 | related_to | undirected | user_confirmed | supports

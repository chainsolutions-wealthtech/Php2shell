# Commit exact 57c8ee6d57efc44fd5cd695c3ef16aa58cfcb7fe

Date UTC 2026-10-28T04:44:03Z; source https://github.com/chainsolutions-wealthtech/Php2shell/commit/57c8ee6d57efc44fd5cd695c3ef16aa58cfcb7fe

Parents: 6368eb5e9b9c5b7837b62cc939a371bf6001a557

Fichiers 1; +16/-0

## .github/workflows/api-contract.yml (added, +16/-0)

Blob 61727f7ee9a79cd3389fecb7ce641e450d27a425; https://github.com/chainsolutions-wealthtech/Php2shell/blob/57c8ee6d57efc44fd5cd695c3ef16aa58cfcb7fe/.github%2Fworkflows%2Fapi-contract.yml

```diff
@@ -0,0 +1,16 @@
+name: api-contract
+on:
+  push:
+  pull_request:
+permissions:
+  contents: read
+jobs:
+  api-contract:
+    runs-on: ubuntu-latest
+    steps:
+      - uses: actions/checkout@v4
+      - uses: actions/setup-python@v5
+        with:
+          python-version: '3.13'
+      - run: python -m pip install -r requirements-api-contract.txt
+      - run: python -m unittest discover -s api_tests -v
```

Attention: inspection du diff Git, sans attestation de tests ou d'exploitation.
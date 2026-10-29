# Commit exact e8e32e2ff0af732d843f3b5ad06ecff5b2cb1d0f

Date UTC 2026-10-28T06:21:06Z; source https://github.com/chainsolutions-wealthtech/Php2shell/commit/e8e32e2ff0af732d843f3b5ad06ecff5b2cb1d0f

Parents: d208aa57e75070cca2314515dc3141fd64c16c34

Fichiers 1; +22/-0

## service/local_api.py (modified, +22/-0)

Blob f3bd8c0df1d9625fe2d0c2c40c66e6660de24409; https://github.com/chainsolutions-wealthtech/Php2shell/blob/e8e32e2ff0af732d843f3b5ad06ecff5b2cb1d0f/service%2Flocal_api.py

```diff
@@ -14,6 +14,7 @@
 from pydantic import BaseModel, ConfigDict, Field
 
 from app.url_intake import preview_url_scope
+from app.public_summary import build_guest_public_summary
 
 
 class PreviewRequest(BaseModel):
@@ -115,6 +116,27 @@ async def preview_url(payload: PreviewRequest, request: Request):
         raise HTTPException(status_code=422, detail="INVALID_URL_PREVIEW") from exc
 
 
+class GuestSummaryRequest(BaseModel):
+    """Strict local-only prototype; external evidence is always UNVERIFIED."""
+    model_config = ConfigDict(extra="forbid", strict=True)
+
+    url: str = Field(min_length=1, max_length=2048)
+    public_response_evidence: dict[str, object] | None = None
+
+
+@app.post("/api/v0.2/guest/summary")
+async def guest_short_summary(payload: GuestSummaryRequest, request: Request):
+    """Return an honest public *preview*, never an audit or stored report."""
+    if (os.getenv("P2S_ENABLE_LOCAL_GUEST_SUMMARY") != "1"
+            or not _is_loopback_peer(request)):
+        raise HTTPException(status_code=403, detail="GUEST_SUMMARY_NOT_AVAILABLE")
+    try:
+        return build_guest_public_summary(
+            payload.url, payload.public_response_evidence)
+    except (ValueError, TypeError) as exc:
+        raise HTTPException(status_code=422, detail="INVALID_GUEST_PREVIEW") from exc
+
+
 class _ActualBodyLimitMiddleware:
     """ASGI request-body bound, independent of Content-Length and chunk framing.
 
```

Attention: inspection du diff Git, sans attestation de tests ou d'exploitation.
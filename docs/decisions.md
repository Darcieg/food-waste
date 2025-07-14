### Decision: S3 file existence check (upload step)
**Date:** 2025-07-12  
**Context:** Uploading CSVs from `data/solutions/` to S3  
**Decision:** Use `head_object()` to check if a file exists before uploading.

**Rationale:**
- Dataset is small and static for now
- Performance is not a bottleneck
- Avoids need for a local manifest or sync tracking
- Simplifies logic in the short term

**Alternatives considered:**
- Local JSON manifest (adds state tracking overhead)
- Pre-fetch all S3 keys via `list_objects_v2` (more efficient, but unnecessary for scale)

**Revisit if:**
- Dataset grows significantly
- Uploads become automated or parallelized

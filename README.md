# GitHub Actions - Hands-On Starter

This repo is a step-by-step, copy-paste friendly path to learn CI/CD by doing.
You will complete 3 missions:

---

## Mission 1 - CI for a Python app (tests + artifact)
1) Create a new empty GitHub repo (e.g., ci-cd-demo) - do NOT add templates.
2) Clone it locally and copy these files in.
3) Commit and push. Open the Actions tab - a workflow named CI runs.
4) Inspect logs. Download the uploaded junit-report artifact.

Key files: app.py, tests/test_app.py, .github/workflows/ci.yml

---

## Mission 2 - Build and push a Docker image to GHCR
1) Ensure your repo is public (or enable GHCR permissions for private).
2) Push to main - the Build Docker image workflow will:
   - Log in to GHCR using the GITHUB_TOKEN
   - Build and push the image to ghcr.io/<owner>/<repo>:<sha>
3) Check the Packages tab in your GitHub repo for the image.

Key files: Dockerfile, .github/workflows/docker.yml

---

## Mission 3 - Deploy a static site to GitHub Pages
1) Go to Settings -> Pages and ensure "Build and deployment: GitHub Actions" is selected.
2) Push to main with the provided public/index.html.
3) The "Deploy static site to Pages" workflow will publish your page.
4) The job summary shows the public URL after deploy.

Key files: public/index.html, .github/workflows/pages.yml

---

## What you will learn
- Triggers (on: push, on: pull_request), path filters
- Jobs and runners (runs-on: ubuntu-latest)
- Steps and actions (reusable actions via uses:)
- Artifacts (actions/upload-artifact)
- Caching (actions/setup-python with cache: pip)
- Secrets/Permissions (GHCR via GITHUB_TOKEN)
- Environments (Pages deployment environment)

---

## Quick start

```
# 1) Create an empty repo on GitHub (e.g., ci-cd-demo)
# 2) On your machine:
git clone https://github.com/<your-username>/ci-cd-demo.git
cd ci-cd-demo

# 3) Copy the contents of this starter into your repo folder
# (Unzip the downloaded archive and move the files here.)

# 4) Commit and push
git add .
git commit -m "Add CI/CD hands-on starter"
git push origin main
```

Open GitHub -> Actions tab -> watch jobs run live.

---

## Change the app and tests
Edit app.py response text and watch tests fail/pass.
Add new tests in tests/. The pipeline runs on every push and PR.

---

## Notes on GHCR permissions
- Public repos: GITHUB_TOKEN can push packages by default.
- Private repos: in Settings -> Actions -> General -> Workflow permissions, enable
  "Read and write permissions". You may also need to grant package permissions in
  Settings -> Packages for your repo/org.

---

## Useful next steps (optional)
- Add a matrix for Python 3.10, 3.11, 3.12
- Require status checks on main (branch protection rules)
- Add code coverage and upload HTML as an artifact
- Add a release workflow on tags (on: push: tags: ["v*"])
- Add a scan step (e.g., Trivy) in the Docker build

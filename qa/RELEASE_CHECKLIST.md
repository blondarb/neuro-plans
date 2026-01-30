# Release Checklist

**checklist_version:** 1.0

Use this checklist before and after each deploy to main. Copy the relevant sections into your run log.

---

## Pre-Deploy

- [ ] All changes committed on feature branch
- [ ] `plans.json` regenerated for any changed plans (`--merge`)
- [ ] JSON validation passed (`--validate-only` shows no errors)
- [ ] Parity check passed for approved plans (`--check-parity`)
- [ ] `mkdocs.yml` nav updated if plans added/moved
- [ ] `docs/plans/index.md` updated if plans added/moved
- [ ] `docs/drafts/queue.md` updated to reflect current state
- [ ] No draft banners on files in `docs/plans/`
- [ ] Frontmatter `status: approved` on all files in `docs/plans/`
- [ ] PR created with descriptive title and summary
- [ ] PR diff reviewed -- no accidental file inclusions (.env, credentials, etc.)

## Deploy

- [ ] PR merged to `main`
- [ ] GitHub Actions deployment completed successfully (`gh run list --limit 1`)

## Post-Deploy

- [ ] **SMK-01:** Site loads without errors
- [ ] **SMK-02:** Plans index renders all categories
- [ ] **SMK-03:** Clinical tool loads, dropdown populated
- [ ] **SMK-04:** Select a plan -- sections and items render
- [ ] **SMK-06:** Mobile layout -- hamburger nav works, tables scroll
- [ ] Spot-check 2-3 changed plans for correct content
- [ ] If new plans added: verify they appear in nav and index
- [ ] If JSON changed: verify clinical tool shows updated data

## Rollback Plan

If critical issues found post-deploy:

1. Revert the merge commit: `git revert <merge-sha> && git push`
2. Verify GitHub Pages rebuilds with reverted state
3. File bug report using `BUG_TEMPLATE.md`

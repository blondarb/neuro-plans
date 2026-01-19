// Firebase Comments Widget for Neuro Plans
// Anonymous comments with upvote/downvote and inline section comments

(async function() {
  console.log('[Comments] Initializing Firebase comments widget...');

  // Track if Firebase is already initialized
  let firebaseInitialized = false;
  let db = null;
  let firebaseModules = null;

  try {
    // Dynamically import Firebase modules
    const { initializeApp, getApps } = await import('https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js');
    firebaseModules = await import('https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js');
    const {
      getFirestore,
      collection,
      addDoc,
      getDocs,
      doc,
      updateDoc,
      deleteDoc,
      query,
      where,
      orderBy,
      increment,
      serverTimestamp
    } = firebaseModules;

    console.log('[Comments] Firebase modules loaded successfully');

    // Firebase configuration
    const firebaseConfig = {
      apiKey: "AIzaSyDmh47osHy-fY2_DP1fiHxen6Kplpx-Vu8",
      authDomain: "neuro-plans.firebaseapp.com",
      projectId: "neuro-plans",
      storageBucket: "neuro-plans.firebasestorage.app",
      messagingSenderId: "412449868431",
      appId: "1:412449868431:web:b41690279a2452d9f83efa"
    };

    // Initialize Firebase only if not already initialized
    let app;
    const existingApps = getApps();
    if (existingApps.length === 0) {
      app = initializeApp(firebaseConfig);
      console.log('[Comments] Firebase initialized (new)');
    } else {
      app = existingApps[0];
      console.log('[Comments] Firebase already initialized, reusing');
    }
    db = getFirestore(app);
    firebaseInitialized = true;

    // Store all comments for the page
    let allComments = [];

    // Get current page identifier
    function getPageId() {
      const path = window.location.pathname
        .replace(/\//g, '_')
        .replace(/\.html$/, '')
        .replace(/\.md$/, '')
        .replace(/^_/, '')
        .replace(/_$/, '') || 'home';
      return path;
    }

    // Get user's vote history from localStorage
    function getVoteHistory() {
      const history = localStorage.getItem('neuro_plans_votes');
      return history ? JSON.parse(history) : {};
    }

    // Save vote to localStorage
    function saveVote(commentId, voteType) {
      const history = getVoteHistory();
      history[commentId] = voteType;
      localStorage.setItem('neuro_plans_votes', JSON.stringify(history));
    }

    // Format timestamp
    function formatDate(timestamp) {
      if (!timestamp) return 'Just now';
      const date = timestamp.toDate ? timestamp.toDate() : new Date(timestamp);
      const now = new Date();
      const diff = now - date;

      if (diff < 60000) return 'Just now';
      if (diff < 3600000) return `${Math.floor(diff / 60000)}m ago`;
      if (diff < 86400000) return `${Math.floor(diff / 3600000)}h ago`;
      if (diff < 604800000) return `${Math.floor(diff / 86400000)}d ago`;

      return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
    }

    // Escape HTML to prevent XSS
    function escapeHtml(text) {
      const div = document.createElement('div');
      div.textContent = text;
      return div.innerHTML;
    }

    // Create comment HTML
    function createCommentHTML(comment, id, compact = false) {
      const voteHistory = getVoteHistory();
      const userVote = voteHistory[id];

      if (compact) {
        return `
          <div class="comment-item compact" data-id="${id}">
            <div class="comment-header">
              <span class="comment-author">${escapeHtml(comment.author || 'Anonymous')}</span>
              <span class="comment-date">${formatDate(comment.createdAt)}</span>
              <button class="delete-btn" data-id="${id}" title="Delete comment">🗑️</button>
            </div>
            <div class="comment-body">${escapeHtml(comment.body)}</div>
            <div class="comment-actions">
              <button class="vote-btn upvote ${userVote === 'up' ? 'voted' : ''}" data-id="${id}" data-vote="up">
                <span>👍</span>
                <span class="vote-count">${comment.upvotes || 0}</span>
              </button>
              <button class="vote-btn downvote ${userVote === 'down' ? 'voted' : ''}" data-id="${id}" data-vote="down">
                <span>👎</span>
                <span class="vote-count">${comment.downvotes || 0}</span>
              </button>
            </div>
          </div>
        `;
      }

      return `
        <div class="comment-item" data-id="${id}">
          <div class="comment-header">
            <span class="comment-author">${escapeHtml(comment.author || 'Anonymous')}</span>
            <span class="comment-date">${formatDate(comment.createdAt)}</span>
            <button class="delete-btn" data-id="${id}" title="Delete comment">🗑️</button>
          </div>
          ${comment.section ? `<span class="comment-section-tag">Re: ${escapeHtml(comment.section)}</span>` : ''}
          <div class="comment-body">${escapeHtml(comment.body)}</div>
          <div class="comment-actions">
            <button class="vote-btn upvote ${userVote === 'up' ? 'voted' : ''}" data-id="${id}" data-vote="up">
              <span>👍</span>
              <span class="vote-count">${comment.upvotes || 0}</span>
            </button>
            <button class="vote-btn downvote ${userVote === 'down' ? 'voted' : ''}" data-id="${id}" data-vote="down">
              <span>👎</span>
              <span class="vote-count">${comment.downvotes || 0}</span>
            </button>
          </div>
        </div>
      `;
    }

    // Get comments for a specific section
    function getCommentsForSection(sectionName) {
      return allComments.filter(c => c.section === sectionName);
    }

    // Load all comments for current page
    async function loadAllComments() {
      const pageId = getPageId();

      try {
        console.log('[Comments] Loading all comments for page:', pageId);

        const q = query(
          collection(db, 'comments'),
          where('pageId', '==', pageId)
        );

        const snapshot = await getDocs(q);
        console.log('[Comments] Found', snapshot.size, 'comments');

        allComments = [];
        snapshot.forEach(docSnap => {
          allComments.push({ id: docSnap.id, ...docSnap.data() });
        });

        // Sort by createdAt descending (newest first)
        allComments.sort((a, b) => {
          const aTime = a.createdAt?.toMillis?.() || 0;
          const bTime = b.createdAt?.toMillis?.() || 0;
          return bTime - aTime;
        });

        return allComments;

      } catch (error) {
        console.error('[Comments] Error loading comments:', error);
        return [];
      }
    }

    // Update comment counts on all section badges
    function updateSectionBadges() {
      document.querySelectorAll('.inline-comment-btn').forEach(btn => {
        const section = btn.dataset.section;
        const count = getCommentsForSection(section).length;
        const badge = btn.querySelector('.comment-badge');
        if (badge) {
          badge.textContent = count;
          badge.style.display = count > 0 ? 'inline-flex' : 'none';
        }
      });

      // Update main comment count
      const commentCount = document.getElementById('comment-count');
      if (commentCount) {
        commentCount.textContent = `(${allComments.length})`;
      }
    }

    // Render comments in the main list
    function renderMainCommentList() {
      const commentList = document.getElementById('comment-list');
      if (!commentList) return;

      if (allComments.length === 0) {
        commentList.innerHTML = '<div class="no-comments">No comments yet. Be the first to share your feedback!</div>';
        return;
      }

      let html = '';
      allComments.forEach(comment => {
        html += createCommentHTML(comment, comment.id);
      });

      commentList.innerHTML = html;
      attachVoteHandlers();
    }

    // Create inline comment popup for a section
    function showInlineCommentPopup(sectionName, anchorElement) {
      // Remove any existing popup
      closeAllPopups();

      const sectionComments = getCommentsForSection(sectionName);

      const popup = document.createElement('div');
      popup.className = 'inline-comment-popup';
      popup.innerHTML = `
        <div class="popup-header">
          <span class="popup-title">💬 Comments: ${escapeHtml(sectionName)}</span>
          <button class="popup-close" title="Close">&times;</button>
        </div>
        <div class="popup-comments">
          ${sectionComments.length === 0
            ? '<div class="no-section-comments">No comments on this section yet.</div>'
            : sectionComments.map(c => createCommentHTML(c, c.id, true)).join('')
          }
        </div>
        <form class="popup-form">
          <input type="text" class="popup-author" placeholder="Your name (optional)" maxlength="50">
          <textarea class="popup-body" placeholder="Add your feedback on this section..." required maxlength="1000"></textarea>
          <div class="popup-actions">
            <button type="submit" class="popup-submit">Submit</button>
            <button type="button" class="popup-cancel">Cancel</button>
          </div>
        </form>
      `;

      // Position popup near the anchor
      document.body.appendChild(popup);

      const rect = anchorElement.getBoundingClientRect();
      const popupRect = popup.getBoundingClientRect();

      // Position below the heading, aligned left
      let top = rect.bottom + window.scrollY + 8;
      let left = rect.left + window.scrollX;

      // Keep within viewport
      if (left + popupRect.width > window.innerWidth - 20) {
        left = window.innerWidth - popupRect.width - 20;
      }
      if (left < 20) left = 20;

      popup.style.top = `${top}px`;
      popup.style.left = `${left}px`;

      // Attach event handlers
      popup.querySelector('.popup-close').addEventListener('click', closeAllPopups);
      popup.querySelector('.popup-cancel').addEventListener('click', closeAllPopups);

      popup.querySelector('.popup-form').addEventListener('submit', async (e) => {
        e.preventDefault();
        const author = popup.querySelector('.popup-author').value.trim() || 'Anonymous';
        const body = popup.querySelector('.popup-body').value.trim();

        if (!body) return;

        const submitBtn = popup.querySelector('.popup-submit');
        submitBtn.disabled = true;
        submitBtn.textContent = 'Submitting...';

        try {
          await addDoc(collection(db, 'comments'), {
            pageId: getPageId(),
            author: author,
            body: body,
            section: sectionName,
            upvotes: 0,
            downvotes: 0,
            createdAt: serverTimestamp()
          });

          // Reload comments and update UI
          await loadAllComments();
          updateSectionBadges();
          renderMainCommentList();
          closeAllPopups();

          // Show toast
          showToast('Comment added successfully!');

        } catch (error) {
          console.error('[Comments] Error submitting:', error);
          alert('Failed to submit comment: ' + error.message);
          submitBtn.disabled = false;
          submitBtn.textContent = 'Submit';
        }
      });

      // Attach vote handlers in popup
      popup.querySelectorAll('.vote-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          const commentId = btn.dataset.id;
          const voteType = btn.dataset.vote;
          handleVote(commentId, voteType);
        });
      });

      // Attach delete handlers in popup
      popup.querySelectorAll('.delete-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          const commentId = btn.dataset.id;
          handleDelete(commentId);
        });
      });

      // Close on click outside
      setTimeout(() => {
        document.addEventListener('click', handleOutsideClick);
      }, 100);
    }

    function handleOutsideClick(e) {
      const popup = document.querySelector('.inline-comment-popup');
      const btn = e.target.closest('.inline-comment-btn');
      if (popup && !popup.contains(e.target) && !btn) {
        closeAllPopups();
      }
    }

    function closeAllPopups() {
      document.querySelectorAll('.inline-comment-popup').forEach(p => p.remove());
      document.removeEventListener('click', handleOutsideClick);
    }

    function showToast(message) {
      const toast = document.createElement('div');
      toast.className = 'comment-toast';
      toast.textContent = message;
      document.body.appendChild(toast);
      setTimeout(() => toast.classList.add('show'), 10);
      setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => toast.remove(), 300);
      }, 2500);
    }

    // Handle voting
    async function handleVote(commentId, voteType) {
      const voteHistory = getVoteHistory();
      const previousVote = voteHistory[commentId];

      if (previousVote === voteType) return;

      const commentRef = doc(db, 'comments', commentId);

      try {
        const updates = {};

        if (voteType === 'up') {
          updates.upvotes = increment(1);
        } else {
          updates.downvotes = increment(1);
        }

        if (previousVote === 'up') {
          updates.upvotes = increment(-1);
        } else if (previousVote === 'down') {
          updates.downvotes = increment(-1);
        }

        await updateDoc(commentRef, updates);
        saveVote(commentId, voteType);

        // Update all instances of this comment in the UI
        document.querySelectorAll(`.comment-item[data-id="${commentId}"]`).forEach(commentEl => {
          const upBtn = commentEl.querySelector('.vote-btn.upvote');
          const downBtn = commentEl.querySelector('.vote-btn.downvote');

          upBtn.classList.toggle('voted', voteType === 'up');
          downBtn.classList.toggle('voted', voteType === 'down');

          const upCount = upBtn.querySelector('.vote-count');
          const downCount = downBtn.querySelector('.vote-count');

          if (voteType === 'up') {
            upCount.textContent = parseInt(upCount.textContent) + 1;
            if (previousVote === 'down') {
              downCount.textContent = parseInt(downCount.textContent) - 1;
            }
          } else {
            downCount.textContent = parseInt(downCount.textContent) + 1;
            if (previousVote === 'up') {
              upCount.textContent = parseInt(upCount.textContent) - 1;
            }
          }
        });

      } catch (error) {
        console.error('[Comments] Error voting:', error);
      }
    }

    /**
     * Show delete confirmation dialog
     * Returns a promise that resolves to true if user confirms, false otherwise
     */
    function showDeleteConfirmation() {
      return new Promise((resolve) => {
        // Create overlay
        const overlay = document.createElement('div');
        overlay.className = 'delete-confirm-overlay';
        overlay.innerHTML = `
          <div class="delete-confirm-dialog">
            <div class="delete-confirm-icon">⚠️</div>
            <h3 class="delete-confirm-title">Delete Comment?</h3>
            <p class="delete-confirm-message">
              This action is <strong>permanent</strong> and cannot be undone.
            </p>
            <p class="delete-confirm-warning">
              Please only delete comments that you created. Do not delete other people's comments.
            </p>
            <div class="delete-confirm-actions">
              <button class="delete-confirm-cancel">Cancel</button>
              <button class="delete-confirm-delete">Delete Permanently</button>
            </div>
          </div>
        `;

        document.body.appendChild(overlay);

        // Animate in
        requestAnimationFrame(() => overlay.classList.add('show'));

        // Handle buttons
        overlay.querySelector('.delete-confirm-cancel').addEventListener('click', () => {
          overlay.classList.remove('show');
          setTimeout(() => overlay.remove(), 200);
          resolve(false);
        });

        overlay.querySelector('.delete-confirm-delete').addEventListener('click', () => {
          overlay.classList.remove('show');
          setTimeout(() => overlay.remove(), 200);
          resolve(true);
        });

        // Close on overlay click
        overlay.addEventListener('click', (e) => {
          if (e.target === overlay) {
            overlay.classList.remove('show');
            setTimeout(() => overlay.remove(), 200);
            resolve(false);
          }
        });
      });
    }

    /**
     * Handle comment deletion with confirmation
     */
    async function handleDelete(commentId) {
      const confirmed = await showDeleteConfirmation();
      if (!confirmed) return;

      try {
        const commentRef = doc(db, 'comments', commentId);
        await deleteDoc(commentRef);

        // Reload comments and update UI
        await loadAllComments();
        updateSectionBadges();
        renderMainCommentList();
        updateTocCommentBadges();
        closeAllPopups();

        showToast('Comment deleted');
      } catch (error) {
        console.error('[Comments] Error deleting comment:', error);
        alert('Failed to delete comment: ' + error.message);
      }
    }

    // Attach vote handlers to buttons
    function attachVoteHandlers() {
      document.querySelectorAll('.comment-list .vote-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          const commentId = btn.dataset.id;
          const voteType = btn.dataset.vote;
          handleVote(commentId, voteType);
        });
      });

      // Attach delete handlers
      document.querySelectorAll('.comment-list .delete-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          const commentId = btn.dataset.id;
          handleDelete(commentId);
        });
      });
    }

    // Add inline comment buttons to main section headings (h2 only)
    // This matches the TOC which only shows h2 headings (toc_depth: 2 in mkdocs.yml)
    function addInlineCommentButtons() {
      // Only add to h2 headings (main sections), not h3 subheadings
      const headings = document.querySelectorAll('h2');

      headings.forEach(heading => {
        const text = heading.textContent.trim();

        // Skip comment-related headings
        if (text.includes('Comments') || text.includes('Feedback') || text.includes('Change Log')) {
          return;
        }

        // Skip if already has a button
        if (heading.querySelector('.inline-comment-btn')) {
          return;
        }

        const btn = document.createElement('button');
        btn.className = 'inline-comment-btn';
        btn.dataset.section = text;
        btn.title = `Comment on "${text}"`;
        btn.innerHTML = `
          <span class="comment-icon">💬</span>
          <span class="comment-badge" style="display: none;">0</span>
        `;

        btn.addEventListener('click', (e) => {
          e.preventDefault();
          e.stopPropagation();
          showInlineCommentPopup(text, heading);
        });

        heading.appendChild(btn);
      });

      console.log('[Comments] Added inline comment buttons to', headings.length, 'h2 headings');
    }

    // Submit from main form
    async function submitMainComment(event) {
      event.preventDefault();

      const form = event.target;
      const submitBtn = form.querySelector('button[type="submit"]');
      const author = form.querySelector('#comment-author').value.trim() || 'Anonymous';
      const body = form.querySelector('#comment-body').value.trim();
      const section = form.querySelector('#comment-section')?.value || '';

      if (!body) {
        alert('Please enter a comment');
        return;
      }

      submitBtn.disabled = true;
      submitBtn.textContent = 'Submitting...';

      try {
        await addDoc(collection(db, 'comments'), {
          pageId: getPageId(),
          author: author,
          body: body,
          section: section,
          upvotes: 0,
          downvotes: 0,
          createdAt: serverTimestamp()
        });

        form.reset();
        await loadAllComments();
        updateSectionBadges();
        renderMainCommentList();
        showToast('Comment added successfully!');

      } catch (error) {
        console.error('[Comments] Error submitting comment:', error);
        alert('Failed to submit comment: ' + error.message);
      } finally {
        submitBtn.disabled = false;
        submitBtn.textContent = 'Submit Comment';
      }
    }

    // Get main sections from current page for dropdown (h2 only)
    function getSections() {
      const sections = [];
      document.querySelectorAll('h2').forEach(heading => {
        const text = heading.textContent.trim()
          .replace(/💬\s*\d*$/, '') // Remove any trailing comment icons
          .trim();
        if (text && !text.includes('Comments') && !text.includes('Feedback') && !text.includes('Change Log')) {
          sections.push(text);
        }
      });
      return sections;
    }

    // Initialize comment widget
    async function initComments() {
      // Check if we're on a page with comments container
      const container = document.getElementById('comments-container');

      // Add inline buttons to all section headings regardless of container
      addInlineCommentButtons();

      // Load all comments
      await loadAllComments();
      updateSectionBadges();

      if (!container) {
        console.log('[Comments] No comments-container, inline comments only');
        return;
      }

      console.log('[Comments] Found comments-container, initializing full widget');

      const sections = getSections();
      const sectionOptions = sections.length > 0
        ? `<option value="">General feedback</option>${sections.map(s => `<option value="${escapeHtml(s)}">${escapeHtml(s)}</option>`).join('')}`
        : '';

      container.innerHTML = `
        <div class="comment-section">
          <h3>💬 All Feedback & Comments <span id="comment-count" style="font-weight: normal; color: #64748b;">(${allComments.length})</span></h3>
          <p class="comment-tip">Tip: Click the 💬 icon next to any section heading to comment directly on that section.</p>

          <form class="comment-form" id="comment-form">
            <input type="text" id="comment-author" placeholder="Your name (optional)" maxlength="50">
            ${sections.length > 0 ? `
            <select id="comment-section">
              ${sectionOptions}
            </select>
            ` : '<input type="hidden" id="comment-section" value="">'}
            <textarea id="comment-body" placeholder="Share your feedback, suggestions, or questions about this plan..." required maxlength="1000"></textarea>
            <button type="submit">Submit Comment</button>
          </form>

          <div class="comment-list" id="comment-list">
            <div class="loading-spinner"></div>
          </div>
        </div>
      `;

      // Attach form handler
      document.getElementById('comment-form').addEventListener('submit', submitMainComment);

      // Render comments
      renderMainCommentList();
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', initComments);
    } else {
      initComments();
    }

    /**
     * Normalize section name by removing pilcrow (¶) and trimming whitespace
     */
    function normalizeSectionName(name) {
      if (!name) return '';
      return name.replace(/¶/g, '').trim();
    }

    /**
     * Update TOC badges to show which sections have comments
     * Shows badges on the right-side table of contents (section links within the page)
     * Only shows badge on sections that have comments
     */
    function updateTocCommentBadges() {
      try {
        // Group comments by normalized section name
        const commentCountsBySection = {};
        allComments.forEach(comment => {
          const section = normalizeSectionName(comment.section);
          if (section) {
            commentCountsBySection[section] = (commentCountsBySection[section] || 0) + 1;
          }
        });

        console.log('[Comments] Comment counts by section (normalized):', commentCountsBySection);

        // Find the right-side table of contents (MkDocs Material uses .md-sidebar--secondary for the right TOC)
        // The TOC links are anchor links to headings on the current page
        const tocContainer = document.querySelector('.md-sidebar--secondary .md-nav--secondary');
        if (!tocContainer) {
          console.log('[Comments] No secondary TOC found on this page');
          return;
        }

        // Find all TOC links (these link to #anchor on the current page)
        const tocLinks = tocContainer.querySelectorAll('.md-nav__link');
        const tocTexts = Array.from(tocLinks).map(l => l.textContent.trim()).slice(0, 10);
        console.log('[Comments] Found', tocLinks.length, 'TOC links, first 10:', tocTexts);

        tocLinks.forEach(link => {
          const href = link.getAttribute('href');
          if (!href || !href.startsWith('#')) return;

          // Get the section name from the link text and normalize it
          const rawText = link.textContent.trim();
          const sectionName = normalizeSectionName(rawText);

          // Remove any existing badge first
          const existingBadge = link.querySelector('.toc-comment-badge');
          if (existingBadge) {
            existingBadge.remove();
          }

          // Check if this section has comments (try exact match first, then partial)
          let count = commentCountsBySection[sectionName] || 0;

          // If no exact match, try to find a partial match (for cases where section names differ slightly)
          if (count === 0) {
            for (const [storedSection, c] of Object.entries(commentCountsBySection)) {
              if (storedSection.includes(sectionName) || sectionName.includes(storedSection)) {
                count = c;
                break;
              }
            }
          }

          if (count > 0) {
            const badge = document.createElement('span');
            badge.className = 'toc-comment-badge';
            badge.textContent = count;
            const tooltipText = `${count} comment${count > 1 ? 's' : ''} - click to view`;
            badge.title = tooltipText;
            badge.setAttribute('data-tooltip', tooltipText);
            link.appendChild(badge);
            console.log('[Comments] TOC badge added:', sectionName, '=', count);
          }
        });

      } catch (error) {
        console.error('[Comments] Error updating TOC badges:', error);
      }
    }

    /**
     * Update left navigation badges to show which pages have comments
     * Shows badges on the left sidebar navigation (page links)
     */
    async function updateLeftNavBadges() {
      try {
        // Get all comments grouped by pageId (across all pages)
        const allDocsQuery = query(collection(db, 'comments'));
        const snapshot = await getDocs(allDocsQuery);

        const commentCountsByPage = {};
        snapshot.forEach(docSnap => {
          const data = docSnap.data();
          const pageId = data.pageId;
          commentCountsByPage[pageId] = (commentCountsByPage[pageId] || 0) + 1;
        });

        console.log('[Comments] Left nav - comment counts by page:', commentCountsByPage);

        // Find all nav links in the left sidebar (not the right TOC)
        // Left sidebar uses .md-sidebar--primary
        const leftNav = document.querySelector('.md-sidebar--primary');
        if (!leftNav) {
          console.log('[Comments] No left navigation found');
          return;
        }

        leftNav.querySelectorAll('.md-nav__link').forEach(link => {
          const href = link.getAttribute('href');
          if (!href || href === '#' || href.startsWith('javascript:') || href.startsWith('#')) return;

          // Convert href to pageId format - handle relative paths
          let pageId = href
            .replace(/^\.\.\//, '')
            .replace(/^\.\//, '')
            .replace(/\//g, '_')
            .replace(/\.html$/, '')
            .replace(/\.md$/, '')
            .replace(/^_/, '')
            .replace(/_$/, '')
            .replace(/_index$/, '');

          // Also try extracting just the page name from the path
          const pathParts = href.replace(/\/$/, '').split('/');
          const pageName = pathParts[pathParts.length - 1] || pathParts[pathParts.length - 2];

          // Build exact match variations
          const pageIdVariations = [
            pageId,
            'neuro-plans_' + pageId,
            pageId.replace(/^plans_/, 'neuro-plans_plans_'),
            pageId.replace(/^drafts_/, 'neuro-plans_drafts_'),
            'neuro-plans_plans_' + pageName,
            'neuro-plans_drafts_' + pageName,
            'plans_' + pageName,
            'drafts_' + pageName
          ];

          // Find matching count
          let count = 0;
          for (const variant of pageIdVariations) {
            if (commentCountsByPage[variant]) {
              count = commentCountsByPage[variant];
              break;
            }
          }

          // Remove any existing badge first
          const existingBadge = link.querySelector('.toc-comment-badge');
          if (existingBadge) {
            existingBadge.remove();
          }

          if (count > 0) {
            const badge = document.createElement('span');
            badge.className = 'toc-comment-badge';
            badge.textContent = count;
            const tooltipText = `${count} comment${count > 1 ? 's' : ''} on this page`;
            badge.title = tooltipText;
            badge.setAttribute('data-tooltip', tooltipText);
            link.appendChild(badge);
            console.log('[Comments] Left nav badge added for:', href, '=', count);
          }
        });

      } catch (error) {
        console.error('[Comments] Error updating left nav badges:', error);
      }
    }

    // Export for use in other scripts
    window.NeuroComments = {
      loadAllComments,
      updateSectionBadges,
      renderMainCommentList,
      showInlineCommentPopup,
      handleVote,
      updateTocCommentBadges,
      updateLeftNavBadges,
      reinitialize: fullReinitialize
    };

    // Update badges after a short delay to ensure nav is rendered
    setTimeout(() => {
      updateTocCommentBadges();
      updateLeftNavBadges();
    }, 500);

    // ========================================
    // MKDOCS INSTANT NAVIGATION SUPPORT
    // ========================================
    // MkDocs Material's instant navigation doesn't reload the page,
    // so we need to reinitialize comments when navigating between pages.

    // Track current page to detect navigation
    let currentPage = window.location.pathname;
    let isReinitializing = false; // Prevent re-entrancy

    // Full reinitialization function
    async function fullReinitialize() {
      const pageId = getPageId();
      console.log('[Comments] Full reinitialize called for:', window.location.pathname, '(pageId:', pageId, ')');

      // Reset comments array for new page
      allComments = [];

      // Remove old inline buttons (they have stale event handlers)
      document.querySelectorAll('.inline-comment-btn').forEach(btn => btn.remove());

      // Remove old TOC badges
      document.querySelectorAll('.toc-comment-badge').forEach(badge => badge.remove());

      // Wait for MkDocs Material to finish rendering new content
      // Check that the page title or h1 matches the new page
      let attempts = 0;
      const maxAttempts = 10;
      while (attempts < maxAttempts) {
        const h1 = document.querySelector('article h1, .md-content h1');
        const article = document.querySelector('article.md-content__inner');
        if (h1 && article) {
          console.log('[Comments] DOM ready, found h1:', h1.textContent.substring(0, 30));
          break;
        }
        console.log('[Comments] Waiting for DOM... attempt', attempts + 1);
        await new Promise(resolve => setTimeout(resolve, 100));
        attempts++;
      }

      // Reinitialize
      await initComments();

      // Update badges
      updateTocCommentBadges();
      await updateLeftNavBadges();

      console.log('[Comments] Reinitialize complete for', pageId, '- comments loaded:', allComments.length);
    }

    // Reinitialize comments on page change
    function reinitializeOnNavigation() {
      const newPage = window.location.pathname;

      // Skip if same page or already reinitializing
      if (newPage === currentPage) {
        return; // Same page, no action needed
      }

      if (isReinitializing) {
        console.log('[Comments] Already reinitializing, queued check for:', newPage);
        // Queue another check in case URL changes during reinit
        setTimeout(() => reinitializeOnNavigation(), 400);
        return;
      }

      console.log('[Comments] PAGE CHANGED:', currentPage, '->', newPage);
      currentPage = newPage;
      isReinitializing = true;

      // Delay to let MkDocs finish rendering the new content
      setTimeout(async () => {
        try {
          await fullReinitialize();
        } catch (err) {
          console.error('[Comments] Error during reinitialize:', err);
        } finally {
          // Always reset the flag after a delay
          setTimeout(() => {
            isReinitializing = false;
          }, 300);
        }
      }, 250);
    }

    // ========================================
    // MULTIPLE NAVIGATION DETECTION METHODS
    // ========================================
    // MkDocs Material instant navigation is tricky - we use multiple methods

    // Method 1: Listen for popstate (browser back/forward)
    window.addEventListener('popstate', () => {
      console.log('[Comments] popstate event fired, URL:', window.location.pathname);
      setTimeout(() => {
        reinitializeOnNavigation();
      }, 150);
    });

    // Method 2: MkDocs Material subscription-based navigation
    // This is the official way to detect instant navigation in MkDocs Material
    if (typeof document$ !== 'undefined') {
      document$.subscribe(() => {
        console.log('[Comments] document$ subscription fired, URL:', window.location.pathname);
        setTimeout(() => {
          reinitializeOnNavigation();
        }, 150);
      });
    }

    // Method 3: Watch for URL hash changes
    window.addEventListener('hashchange', () => {
      console.log('[Comments] hashchange fired');
    });

    // Method 4: Listen for clicks on navigation links
    document.addEventListener('click', (e) => {
      const link = e.target.closest('a[href]');
      if (link) {
        const href = link.getAttribute('href');
        // Internal link (not anchor, not external)
        if (href && !href.startsWith('#') && !href.startsWith('http') && !href.startsWith('javascript')) {
          console.log('[Comments] Internal link clicked:', href);
          // Schedule reinit check after navigation completes
          setTimeout(() => {
            reinitializeOnNavigation();
          }, 300);
          setTimeout(() => {
            reinitializeOnNavigation();
          }, 600);
        }
      }
    });

    // Method 5: Observe the main content container being replaced
    const setupContentObserver = () => {
      // MkDocs Material replaces the content inside .md-content
      const contentContainer = document.querySelector('.md-content');
      if (contentContainer) {
        const observer = new MutationObserver((mutations) => {
          // Only trigger if h1 or h2 changed (indicating new page)
          for (const mutation of mutations) {
            if (mutation.type === 'childList') {
              for (const node of mutation.addedNodes) {
                if (node.nodeType === 1 && (node.tagName === 'ARTICLE' || node.querySelector && node.querySelector('h1, h2'))) {
                  console.log('[Comments] Content replaced (article/heading detected)');
                  setTimeout(() => {
                    reinitializeOnNavigation();
                  }, 150);
                  return;
                }
              }
            }
          }
        });
        observer.observe(contentContainer, { childList: true, subtree: true });
        console.log('[Comments] Content observer set up on .md-content');
      }
    };

    // Set up content observer
    setupContentObserver();

    // Method 6: Periodic check as fallback (every 500ms for reliability)
    setInterval(() => {
      const newPath = window.location.pathname;
      if (newPath !== currentPage && !isReinitializing) {
        console.log('[Comments] Periodic check detected page change:', currentPage, '->', newPath);
        reinitializeOnNavigation();
      }
    }, 500);

    // Method 7: Also check when the page title changes (another indicator of navigation)
    const titleObserver = new MutationObserver(() => {
      const newPath = window.location.pathname;
      if (newPath !== currentPage && !isReinitializing) {
        console.log('[Comments] Title change detected, reinitializing');
        reinitializeOnNavigation();
      }
    });
    const titleEl = document.querySelector('title');
    if (titleEl) {
      titleObserver.observe(titleEl, { childList: true, characterData: true, subtree: true });
    }

  } catch (error) {
    console.error('[Comments] Fatal error initializing comments:', error);

    const container = document.getElementById('comments-container');
    if (container) {
      container.innerHTML = `
        <div class="comment-section">
          <h3>💬 Feedback & Comments</h3>
          <div class="no-comments" style="color: #dc2626;">
            Error loading comments system: ${error.message}<br>
            <small>Please check browser console for details.</small>
          </div>
        </div>
      `;
    }
  }

})();

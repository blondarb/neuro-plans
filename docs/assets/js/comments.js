// Firebase Comments Widget for Neuro Plans
// Anonymous comments with upvote/downvote and inline section comments

(async function() {
  console.log('[Comments] Initializing Firebase comments widget...');

  try {
    // Dynamically import Firebase modules
    const { initializeApp } = await import('https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js');
    const {
      getFirestore,
      collection,
      addDoc,
      getDocs,
      doc,
      updateDoc,
      query,
      where,
      orderBy,
      increment,
      serverTimestamp
    } = await import('https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js');

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

    // Initialize Firebase
    const app = initializeApp(firebaseConfig);
    const db = getFirestore(app);
    console.log('[Comments] Firebase initialized');

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

    // Attach vote handlers to buttons
    function attachVoteHandlers() {
      document.querySelectorAll('.comment-list .vote-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          const commentId = btn.dataset.id;
          const voteType = btn.dataset.vote;
          handleVote(commentId, voteType);
        });
      });
    }

    // Add inline comment buttons to section headings
    function addInlineCommentButtons() {
      const headings = document.querySelectorAll('h2, h3');

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

      console.log('[Comments] Added inline comment buttons to', headings.length, 'headings');
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

    // Get sections from current page for dropdown
    function getSections() {
      const sections = [];
      document.querySelectorAll('h2, h3').forEach(heading => {
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

    // Export for use in other scripts
    window.NeuroComments = {
      loadAllComments,
      updateSectionBadges,
      renderMainCommentList,
      showInlineCommentPopup,
      handleVote
    };

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

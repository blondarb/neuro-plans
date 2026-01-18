// Firebase Comments Widget for Neuro Plans
// Supports anonymous comments with upvote/downvote

import { initializeApp } from 'https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js';
import {
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
} from 'https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js';

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

// Get current page identifier
function getPageId() {
  return window.location.pathname.replace(/\//g, '_').replace(/\.html$/, '') || 'home';
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

// Create comment HTML
function createCommentHTML(comment, id) {
  const voteHistory = getVoteHistory();
  const userVote = voteHistory[id];

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

// Escape HTML to prevent XSS
function escapeHtml(text) {
  const div = document.createElement('div');
  div.textContent = text;
  return div.innerHTML;
}

// Load comments for current page
async function loadComments() {
  const pageId = getPageId();
  const commentList = document.getElementById('comment-list');
  const commentCount = document.getElementById('comment-count');

  if (!commentList) return;

  commentList.innerHTML = '<div class="loading-spinner"></div>';

  try {
    const q = query(
      collection(db, 'comments'),
      where('pageId', '==', pageId),
      orderBy('createdAt', 'desc')
    );

    const snapshot = await getDocs(q);

    if (snapshot.empty) {
      commentList.innerHTML = '<div class="no-comments">No comments yet. Be the first to share your feedback!</div>';
      if (commentCount) commentCount.textContent = '0';
      return;
    }

    let html = '';
    snapshot.forEach(doc => {
      html += createCommentHTML(doc.data(), doc.id);
    });

    commentList.innerHTML = html;
    if (commentCount) commentCount.textContent = snapshot.size.toString();

    // Attach vote handlers
    attachVoteHandlers();

  } catch (error) {
    console.error('Error loading comments:', error);
    commentList.innerHTML = '<div class="no-comments">Unable to load comments. Please try again later.</div>';
  }
}

// Submit a new comment
async function submitComment(event) {
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

    // Reset form
    form.reset();

    // Reload comments
    await loadComments();

  } catch (error) {
    console.error('Error submitting comment:', error);
    alert('Failed to submit comment. Please try again.');
  } finally {
    submitBtn.disabled = false;
    submitBtn.textContent = 'Submit Comment';
  }
}

// Handle voting
async function handleVote(commentId, voteType) {
  const voteHistory = getVoteHistory();
  const previousVote = voteHistory[commentId];

  // If clicking same vote, do nothing (can't un-vote)
  if (previousVote === voteType) return;

  const commentRef = doc(db, 'comments', commentId);

  try {
    const updates = {};

    // Add new vote
    if (voteType === 'up') {
      updates.upvotes = increment(1);
    } else {
      updates.downvotes = increment(1);
    }

    // Remove previous vote if exists
    if (previousVote === 'up') {
      updates.upvotes = increment(-1);
    } else if (previousVote === 'down') {
      updates.downvotes = increment(-1);
    }

    await updateDoc(commentRef, updates);

    // Save vote locally
    saveVote(commentId, voteType);

    // Update UI
    const commentEl = document.querySelector(`.comment-item[data-id="${commentId}"]`);
    if (commentEl) {
      const upBtn = commentEl.querySelector('.vote-btn.upvote');
      const downBtn = commentEl.querySelector('.vote-btn.downvote');

      // Update button states
      upBtn.classList.toggle('voted', voteType === 'up');
      downBtn.classList.toggle('voted', voteType === 'down');

      // Update counts
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
    }

  } catch (error) {
    console.error('Error voting:', error);
  }
}

// Attach vote handlers to buttons
function attachVoteHandlers() {
  document.querySelectorAll('.vote-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const commentId = btn.dataset.id;
      const voteType = btn.dataset.vote;
      handleVote(commentId, voteType);
    });
  });
}

// Get sections from current page for dropdown
function getSections() {
  const sections = [];
  document.querySelectorAll('h2, h3').forEach(heading => {
    const text = heading.textContent.trim();
    if (text && !text.includes('Comments') && !text.includes('Feedback')) {
      sections.push(text);
    }
  });
  return sections;
}

// Initialize comment widget
function initComments() {
  const container = document.getElementById('comments-container');
  if (!container) return;

  const sections = getSections();
  const sectionOptions = sections.length > 0
    ? `<option value="">General feedback</option>${sections.map(s => `<option value="${escapeHtml(s)}">${escapeHtml(s)}</option>`).join('')}`
    : '';

  container.innerHTML = `
    <div class="comment-section">
      <h3>💬 Feedback & Comments <span id="comment-count" style="font-weight: normal; color: #64748b;">(0)</span></h3>

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
  document.getElementById('comment-form').addEventListener('submit', submitComment);

  // Load existing comments
  loadComments();
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initComments);
} else {
  initComments();
}

// Export for use in other scripts
window.NeuroComments = {
  loadComments,
  submitComment,
  handleVote
};

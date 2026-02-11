// Table Layout Detection
// Adds data-venue-pos attribute to tables based on header column order.
// Venue columns (ED, HOSP, OPD, ICU) appear in different positions
// depending on the table type. This script detects the layout so CSS
// can target venue vs. content columns correctly.

(function() {
  var VENUE_HEADERS = ['ED', 'HOSP', 'OPD', 'ICU'];

  function classifyTables() {
    document.querySelectorAll('table:not([data-venue-pos])').forEach(function(table) {
      var headers = table.querySelectorAll('thead th');
      if (headers.length < 5) return;

      // Get header text (trimmed, uppercase for matching)
      var texts = [];
      for (var i = 0; i < headers.length; i++) {
        texts.push(headers[i].textContent.trim().toUpperCase());
      }

      // Check if last 4 are venue columns
      var lastFour = texts.slice(-4);
      var lastFourAreVenue = lastFour.every(function(t) {
        return VENUE_HEADERS.indexOf(t) !== -1;
      });

      if (lastFourAreVenue) {
        table.setAttribute('data-venue-pos', 'last4');
        return;
      }

      // Check if columns 2-5 (index 1-4) are venue columns
      if (texts.length >= 5) {
        var cols2to5 = texts.slice(1, 5);
        var cols2to5AreVenue = cols2to5.every(function(t) {
          return VENUE_HEADERS.indexOf(t) !== -1;
        });
        if (cols2to5AreVenue) {
          table.setAttribute('data-venue-pos', 'mid');
          return;
        }
      }

      // Check if columns 2-4 (index 1-3) are venue (6-col tables without ICU)
      if (texts.length >= 4) {
        var cols2to4 = texts.slice(1, 4);
        var cols2to4AreVenue = cols2to4.every(function(t) {
          return VENUE_HEADERS.indexOf(t) !== -1;
        });
        if (cols2to4AreVenue) {
          table.setAttribute('data-venue-pos', 'mid3');
          return;
        }
      }
    });
  }

  // Detect scrollable tables and add affordance hints
  function markScrollableTables() {
    document.querySelectorAll('.md-typeset table:not([class])').forEach(function(table) {
      if (table.scrollWidth > table.clientWidth + 2) {
        table.setAttribute('data-scrollable', 'true');

        // Add swipe hint if not already present and no previous scroll
        if (!table.previousElementSibling || !table.previousElementSibling.classList.contains('table-scroll-hint')) {
          var hint = document.createElement('div');
          hint.className = 'table-scroll-hint';
          table.parentNode.insertBefore(hint, table);
        }

        // Hide hint on first scroll
        table.addEventListener('scroll', function handler() {
          var hint = table.previousElementSibling;
          if (hint && hint.classList.contains('table-scroll-hint')) {
            hint.classList.add('hidden');
          }
          table.removeEventListener('scroll', handler);
        });
      } else {
        table.removeAttribute('data-scrollable');
      }
    });
  }

  function initAll() {
    classifyTables();
    // Delay scroll detection so layout is settled
    setTimeout(markScrollableTables, 200);
  }

  // Run on initial load
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAll);
  } else {
    initAll();
  }

  // Re-run on MkDocs Material instant navigation
  if (typeof document$ !== 'undefined') {
    document$.subscribe(function() {
      setTimeout(initAll, 100);
    });
  }

  // Also observe content changes as fallback
  var content = document.querySelector('.md-content');
  if (content) {
    new MutationObserver(function() {
      classifyTables();
    }).observe(content, { childList: true, subtree: true });
  }

  // Re-check on window resize (orientation change)
  var resizeTimer;
  window.addEventListener('resize', function() {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(markScrollableTables, 250);
  });
})();

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

  // Run on initial load
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', classifyTables);
  } else {
    classifyTables();
  }

  // Re-run on MkDocs Material instant navigation
  if (typeof document$ !== 'undefined') {
    document$.subscribe(function() {
      setTimeout(classifyTables, 100);
    });
  }

  // Also observe content changes as fallback
  var content = document.querySelector('.md-content');
  if (content) {
    new MutationObserver(function() {
      classifyTables();
    }).observe(content, { childList: true, subtree: true });
  }
})();

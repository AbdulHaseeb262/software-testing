Assignment 2 – Q3 Usability Testing Findings

Website Tested
- https://www.wikipedia.org/

Online Tool Used
- Google Lighthouse via https://web.dev/measure (runs Lighthouse audits in the cloud).
- Categories reviewed: Performance, Accessibility, Best Practices, SEO.

Method
- Entered the URL into web.dev/measure and ran an audit.
- Supplemented results with manual heuristic review (navigation clarity, visual consistency, mobile layout).

Key Findings (Qualitative)
Performance
- Strengths:
  - Minimal blocking resources; fast initial render due to lean homepage.
  - Efficient caching and simple layout reduce CPU work.
- Improvements:
  - Defer or async any non-critical scripts when possible.
  - Review any external requests for preconnect/preload opportunities.
  - Ensure images are properly sized and compressed (mostly already excellent on the homepage).

Accessibility
- Strengths:
  - Clear landmarks and headings (search, language tiles, footer segments).
  - Generally good color contrast and readable font sizes.
  - Keyboard navigation works; focus indicators are visible.
- Improvements:
  - Some link texts repeat (e.g., language links); ensure context-rich accessible names where necessary.
  - Continually audit color contrast across all locales/themes.

Best Practices
- Uses secure connections; avoids deprecated APIs.
- Careful use of external resources; no obvious mixed-content issues.
- Improvement area: periodically review console warnings and check for modern image formats where applicable.

SEO
- Clear title, meta tags, and structured content.
- Crawlable content with semantic HTML.
- Suggestion: validate structured data (if used) and ensure alt text quality remains high across localized content.

Heuristic Usability Review (Manual)
- Navigation:
  - Search bar is prominent and central, supporting primary user intent.
  - Global language selection is clear with large, clickable tiles.
- Content density:
  - Concise and scannable; low visual clutter helps quick decision-making.
- Consistency:
  - Design and spacing are consistent, which reduces cognitive load.
- Mobile responsiveness:
  - Homepage adapts well; tiles stack; core actions remain highly visible.
  - Suggest continuous tuning of tap target sizes and spacing for small screens.

Overall Conclusion
- Wikipedia’s homepage demonstrates strong usability and accessibility, with performance benefits from a lean layout.
- The Lighthouse report reinforces strengths in accessibility and best practices, with standard optimization opportunities to consider (deferring non-critical resources, ensuring consistent contrast). Results may vary slightly depending on time and network conditions; you can rerun the audit at web.dev/measure.
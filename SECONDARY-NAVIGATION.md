# Wonder Global Studio — Secondary navigation update

## Start here

Open the combined platform, choose **Secondary**, and follow:

**Subject → Year level → Topic → Activity**

Both Teacher Trial and Secondary Full use this layout. The Primary workspace and the existing Primary/Secondary access codes are unchanged.

## 1. Choose a subject

The Secondary homepage displays **11 subject cards**, not a combined list of lessons:

English; Biology; Chemistry; Physics; Environmental Science; Algebra; Geometry; Trigonometry; Statistics; Philippine History; World History.

Use the **Language**, **Sciences**, **Mathematics**, or **History** filter to narrow the subject cards. **Search subjects** searches names and subject descriptors, not the entire lesson bank.

The **History tracks** navigation shortcut shows just Philippine History and World History. It no longer lists both tracks’ lessons together.

## 2. Choose the year

Opening a subject first shows four year cards: **Secondary 1, 2, 3, and 4**. No topics are displayed until a year is chosen. Topic counts reflect the content included in the current edition.

After choosing a year, the year buttons remain available. Changing the subject returns to that subject’s year selector and clears the previous topic search and region filter.

## 3. Choose a topic

Only topics in the selected **subject and year** appear. Search and region filters apply inside that selection; an empty result does not widen the search to unrelated subjects.

Paired worldwide settings of the same built-in topic share a topic card. For example, the two original location variants of a Biology topic are not displayed as duplicate topic cards. Use **Choose a context** on the activity page to switch between them. The original lesson records and their questions remain intact.

History lessons stay separate, and teacher-created copies are always separate topic cards. Topic grouping does not merge or rewrite learning content.

## 4. Choose an activity

Opening a topic leads to three tabs:

- **Choose activity** — select an available activity format, then use its named Start button or add it to the lesson queue.
- **Lesson overview** — read the original scenario or historical overview, objective, discussion prompt, and, for History, the milestone guide.
- **Sources & notes** — open the retained references and review the content’s provenance.

Filter activity cards by **Practice**, **Study & discuss**, **History skills**, or **Movement** where those categories are available. Only formats allowed for the selected lesson and edition are shown. Existing sensitive-history restrictions still apply.

A small-screen Start bar keeps the selected activity’s start control accessible while scrolling. The original full start panel and lesson-queue button remain available as well.

## Back buttons and tools

The breadcrumb trail and the **Back to [subject] · Secondary [year]** button return to the selected topic list without losing its search or region filter. Returning from a game goes back to that game’s topic.

Same-document browser Back and Forward also restore navigation state when the embedding browser permits history updates. The visible breadcrumb and Back controls remain the dependable alternative in restricted embeds. Leaving an unfinished activity through browser Back asks for confirmation.

**Models & tools** is now organised by subject. Tools shared across subjects remain under **Shared classroom tools**. Subject-model links are also available from relevant topic pages. Model controls, explanations, assumptions, and observation recording are unchanged; models are not assigned artificial year-level requirements.

## What is preserved

The complete Secondary data block is unchanged: **96 lesson packs and 576 question records across 11 subjects**, including all **24 history lessons**. Trial retains **44 lesson packs and 132 question records**, including **8 history samples**. These are stored question records, not a claim that paired contexts contain independent questions.

The Complete subject browser groups those packs into **60 topic cards across subjects and years**; Trial has **44 topic cards**. It never displays that full topic collection together on the homepage.

Primary inputs, gateway access logic, access codes, workspace storage keys, teacher editing, printing, lesson queues, results, and educational-use notices are retained. Existing browser teaching data continues to use the existing storage namespace. Year assignments remain teaching suggestions rather than a certified curriculum map.

## Updating your existing website

1. Extract **Wonder-Global-Studio-Subject-Navigation-GitHub.zip**.
2. Replace the published **index.html** with the new index.html. Keep the existing website address and directory.
3. Refresh the site, open Secondary, and check one Trial lesson. Then check Secondary Full with your existing code.

The ZIP contains the public website only. Do not upload the private Owner Kit, access-code sheets, unlocked Full exports, or the owner’s inputs/source folders. No new access codes were generated for this update.

The platform has not been deployed from this conversation. The downloadable standalone file is the same combined platform as the package’s index.html.

## Editing this interface later

The private Owner Kit contains a new **navigation-extension/** folder with:

- **navigation.js** — subject, year, topic, activity and tool navigation.
- **navigation.css** — layout, responsive rules and component styles.
- **apply_navigation.py** — applies the interface to both Secondary editions while leaving their current JSON data blocks intact.
- **before-navigation-*.html** — the retained runtime baseline used by that patch.
- **content-integrity.json** — the data-preservation check.

From the Owner Kit root, after changing navigation.js or navigation.css:

```sh
python navigation-extension/apply_navigation.py
python source/build_platform.py
```

The build command reuses existing private codes unless explicitly invoked with a rotation option. Publish only the resulting **site/** contents.

The patch uses the retained pre-navigation JavaScript baseline. Edit that baseline deliberately when changing the underlying activity engine; do not expect unrelated manual edits to the patched input script to survive reapplying the patch. Current world-data/config/seed JSON in the input documents is retained. Do not rerun the older, one-off History extension as part of an ordinary UI rebuild.

## Testing boundary

Automated checks cover both editions’ subject/year isolation, topic grouping, activity selection, reference and overview tabs, queues, editor copies, exports, models, responsive layouts, and the existing access-code integration. See the separate test report for exact counts and environment.

The managed test browser blocks localhost and file navigation. Storage checks used an explicit in-memory test adapter; activation checks used a Node Web Crypto bridge. Those adapters are not in the public website. Native browser persistence across restarts, live-site activation and physical webcam/audio operation still need checking on your published site.

---

**Created by: Dr. Wayne Vincent Tolomia**  
For educational purposes only. Not for resale.  
Improvements, suggestions and custom learning web apps: **waynetolomia@gmail.com**

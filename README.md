# Wonder Global Studio
## Primary + Secondary • Trial first • Separate Full access codes

**Created by: Dr. Wayne Vincent Tolomia**  
**Contact: waynetolomia@gmail.com**  
For educational purposes only. Do not resell this web app or any modified version.

## Publish this package

The entire platform, its two trials, and its separately encrypted Full packages are inside **index.html**. There is no build step, server-side code, account system or database to install for the public website.

1. Extract this GitHub upload ZIP on your computer.
2. Create a repository or use a suitable existing repository. Upload **index.html** to its root. Also include **.nojekyll**; the other files in this upload package are safe to publish but optional at runtime.
3. In the repository, open **Settings → Pages**.
4. Under **Build and deployment**, select **Deploy from a branch**, choose **main**, choose **/(root)**, then **Save**.
5. Wait for the Pages deployment and open the website address shown in Pages settings. Keep **Enforce HTTPS** enabled.
6. Open a private browser window to confirm that a new visitor sees **Trial** for both Primary and Secondary. Use the owner’s separate private code sheet to test each Full edition.

Do not upload just the ZIP and expect it to run: upload the extracted HTML file. GitHub Pages serves index.html as the page.

**Never put the private code sheet, owner ZIP, owner inputs, codes.json, old Complete HTML files or old Complete ZIPs in the public repository.** Those files are intentionally not included here. A .gitignore is a convenience, not protection against manual uploads or existing Git history. A clean repository containing only this release’s public package avoids exposing older unencrypted editions.

GitHub Pages is a static-hosting service. It has restrictions on sites primarily facilitating commercial transactions or commercial SaaS. Review those terms before using the platform as a paid service. The same index.html can be hosted on another HTTPS static host.

## Teacher experience

On a new browser, both levels start in Trial. Teachers can explore without entering any code or creating an account.

**Primary Full** and **Secondary Full** use independent access codes. A Primary code cannot decrypt Secondary; a Secondary code cannot decrypt Primary. Teachers can activate one level or both.

Select **Full-version codes → Enter Primary code / Enter Secondary code**, paste the complete code from the author, and select **Unlock**. The default **Remember Full access on this browser** option stores the actual code in that browser’s localStorage. Returning to the same site revalidates the saved code by decrypting the relevant Full package. Changing an “unlocked” flag does not expose Full content.

Uncheck Remember on shared devices to use Full for the current open page only. **Manage access → Forget [level] code** removes only that level’s remembered access on this browser. It does not erase the teaching workspace or affect another person’s device.

An activated teacher can use **Preview trial** and **Return to Full** without deleting or re-entering a remembered code. The other level stays in its own Trial/Full state.

## Browser storage and privacy

Remembered codes are local to the browser profile and website origin. The platform uses an additional installation-path namespace and a separate access record for each level. This namespace is organisation, not isolation from other scripts on the same origin.

Clearing site data, changing browsers or devices, private-browsing lifecycle rules, storage restrictions, moving the site, or changing its hostname can mean the teacher must enter the code again. No account sync is provided.

**The saved code is readable in localStorage.** People using that browser profile, extensions with appropriate access, and other scripts on the same origin may be able to read it. Do not use a personal password as an access code. Do not ask teachers for email, GitHub or banking passwords. No activation code is sent to an activation server by this platform.

The existing apps retain their optional external resource links and hand-tracking downloads. Using the contact link opens an email draft; it does not send an email automatically. The website does not gain a student-account or payment system from this update.

## Teaching workspaces

The latest supplied Global editions are embedded as trusted learning workspaces inside one level-switching platform. Their subject banks, world-context lessons, games, tools and author notices are retained.

Primary and Secondary keep separate lesson data. Trial and Full data are also separate; activating Full does not merge trial results or queues. Neither is deleted. Switching levels asks before abandoning an unfinished activity. Completed records and saved settings are retained when the browser permits storage.

**Edit this homepage** changes the shared welcome page locally. **Export saved homepage** produces another code-protected copy of the platform. It includes the saved welcome-page settings and the encrypted packages, but never saved access codes, activation status or learning history. Save changes before exporting.

Existing Full workspace export buttons can produce **unlocked Full documents**. Those exports are intended for authorised teachers and must be kept private. The outer platform’s encryption does not turn exported Full files into code-gated documents.

## Browser and classroom setup

Use an up-to-date Chrome, Edge, Firefox or Safari and test it on the actual teaching device. Full activation uses **Web Crypto (PBKDF2/SHA-256 and AES-GCM)** and **DecompressionStream (gzip)**. Trial does not depend on decryption. HTTPS or localhost is recommended.

To run locally, use **START-WINDOWS.bat**, **START-MAC.command** or **START-LINUX.sh**, or run:

```sh
python3 serve.py
```

Python 3.10 or later is needed only for that local launcher, not for the hosted website. The launcher binds to the local computer, not the public network. Another port can be selected with `python3 serve.py --port 8010`; a different port is a different browser origin.

Optional camera play still needs explicit browser permission and Internet access to load its existing hand model. Entering an access code never starts a camera. Moving away from the learning workspace stops active camera streams.

## Scope of access control

The public file has separately salted PBKDF2-derived AES-256-GCM encrypted Full payloads, not plaintext access codes. Codes are generated randomly with 120 bits of random data plus a stage prefix. Each stage’s code is shared and reusable, with no expiry or device count.

This is **not tamper-proof licensing or DRM**. A person who has a valid code can share it, inspect their browser, or copy decrypted content. There is no individual account revocation, one-device enforcement or central usage tracking. Rotating future codes cannot revoke previous files or historical repository copies.

## Reference documentation

GitHub publishing: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site  
GitHub Pages limits: https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits  
HTTPS: https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https  
localStorage: https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage  
Key derivation: https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/deriveKey  
Authenticated encryption: https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/encrypt

These references explain the platform APIs and hosting setup, not an independent security audit of this app.

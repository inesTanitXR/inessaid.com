# Translation guide for inessaid.com (FR + AR)

The site is Ines Said's personal site. Every English page has a French (/fr/) and Arabic (/ar/) twin,
built by translate.py from i18n/fr.json and i18n/ar.json. Keys are the exact English (HTML, whitespace
collapsed); values are the translation.

## Voice (most important)
Ines writes like her LinkedIn posts: warm, simple, excited, grateful, first person, crediting her team
and volunteers. Short sentences. Exclamation marks are fine ("so happy!"). It must NOT sound like AI or
marketing copy: no em-dashes, no clever taglines, no "not X but Y" constructions, no aphorisms, no
flowery words. Translate the meaning and the feeling naturally, the way she would say it herself in
that language. Do not add or remove facts.

- French: natural, warm, simple French. Address visitors with "vous". Use French typography
  (espace before : ; ! ? is optional, keep it simple), French number format "600 000+", "11 000+".
  Months in French (janv. 2026 / janvier 2026).
- Arabic: Modern Standard Arabic, simple and warm (Tunisian readers should find it natural). Address
  visitors in plural ("ادعوني", "تبرّعوا"). Keep Western digits (600,000+, 2026).
  Arrows flip: "→" / "&rarr;" becomes "←", breadcrumb "›" becomes "‹".

## Keep in Latin script / English (both languages)
Tanit XR, Froliq, Smithsonian, FUTURES, MIT, MIT Reality Hack, AWE, Auggie Awards, Niantic Spatial,
Sketchfab, Oracle, Connected Hub, NYPA, Exelon, Vistra, Davis-Besse, Apple Vision Pro, visionOS,
Meta Quest, WebXR, Unity, PolySpatial, Needle Engine, PortalCam, IEEE, ACM, ISEC, NAAEE,
EE 30 Under 30, Games for Change (G4C), HICC / Heavener International Case Competition, ImmerseGT,
Georgia Tech, ETS / Energy Thought Summit, ELLEvate, Spatial Creator Spotlight, Spatial, LinkedIn,
Instagram, YouTube, GFAA, HEAT, Carthage Magazine, CBS, ABC, UF, NEF, SMUD, FormSubmit, emails, URLs.
Project/work titles stay as-is: Shadows of Tomorrow, Covid Reflections, spARc, Sustainaball, StEVie,
Recyclotopia, BungaLoad, FantasticWinds, Future of Energy and Water, "Art, XR & Impact Opportunities".
In Arabic, job title "Lead XR Developer" stays in English (e.g. "أعمل لدى Froliq بصفة Lead XR Developer").
"XR", "VR", "AR", "3D" stay as Latin abbreviations.
Her name: French "Ines Said"; Arabic body text "إيناس سعيد", but the site brand/logo stays "Ines Said".
Page <title> strings like "About | Ines Said": translate the first part, keep "| Ines Said" in French,
use "| إيناس سعيد" in Arabic.
Places: translate normally (Tunisie / تونس, Nabeul / نابل, El Jem / الجم, Néapolis / نيابوليس,
Carthage / قرطاج, Washington, D.C. / واشنطن العاصمة). Al Jazeera / الجزيرة.
Tunisian Federation of Travel Agencies: Fédération tunisienne des agences de voyages / الجامعة التونسية لوكالات الأسفار.
Fiscal sponsor name "Florida Community Innovation Foundation" stays in English.

## HTML rules
- Keep every tag and attribute exactly (href, class, target, rel, src). Only translate the text between
  tags and the values of alt/title attributes. Same tags, same order where the language allows.
- Keep entities or use the real character (&amp; may become "et" / "و" when it is a word).
- Strings that are only names/brands/numbers: return them unchanged.
- Polaroid captions (2-3 lowercase playful handwritten words like "striking a pose", "soccer time!",
  "with my sister ♡"): keep them just as short and cute, keep the ♡.
- Button labels: short and natural ("Book me to speak" -> "Réserver une intervention" / "احجزوا محاضرة").

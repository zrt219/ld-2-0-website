# LD Speaker Android

Native Android wrapper for the LD Speaker marketing app plus local speaker notes.

## Build contract

- App URL: `LD_APP_URL`, default `http://10.0.2.2:3000`
- Notes mode: `LD_NOTES_MODE=private-seeded|public-blank`
- Package base: `com.lornettedaye.speaker`

The first delivery target is the private seeded APK:

```powershell
$env:JAVA_HOME="C:\Program Files\Android\Android Studio\jbr"
$env:ANDROID_HOME="C:\Users\Zhane\AppData\Local\Android\Sdk"
$env:ANDROID_SDK_ROOT="C:\Users\Zhane\AppData\Local\Android\Sdk"
.\gradlew.bat :app:assemblePrivateSeededDebug -PLD_APP_URL=http://10.0.2.2:3000
```

The public blank-template variant is:

```powershell
.\gradlew.bat :app:assemblePublicBlankDebug -PLD_APP_URL=https://lornettedaye.com
```

The generic selector task honors `LD_NOTES_MODE`:

```powershell
.\gradlew.bat :app:assembleLdSpeakerDebug -PLD_NOTES_MODE=public-blank
```

## App shell

The app has four bottom tabs: `Home`, `Speaking`, `Notes`, and `Book`.
Marketing tabs load the configured web app URL and curated routes from this repo.
`Notes` is native, local-first, and offline-capable.

## Speaker notes

`private-seeded` includes Lornette's two starter talk outlines. `public-blank`
ships the same editable structure without Lornette's seeded content.

Notes persist in app-local `SharedPreferences`. Export actions support copy,
text share, and PDF share from local cache.

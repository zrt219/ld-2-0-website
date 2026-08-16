package com.lornettedaye.speaker

import android.app.Activity
import android.content.ActivityNotFoundException
import android.content.ClipData
import android.content.ClipboardManager
import android.content.Context
import android.content.Intent
import android.graphics.Canvas
import android.graphics.Color
import android.graphics.Paint
import android.graphics.Typeface
import android.graphics.pdf.PdfDocument
import android.net.Uri
import android.os.Bundle
import android.text.InputType
import android.view.Gravity
import android.view.View
import android.view.ViewGroup
import android.webkit.WebResourceRequest
import android.webkit.WebSettings
import android.webkit.WebView
import android.webkit.WebViewClient
import android.widget.Button
import android.widget.EditText
import android.widget.FrameLayout
import android.widget.LinearLayout
import android.widget.ScrollView
import android.widget.TextView
import android.widget.Toast
import org.json.JSONArray
import org.json.JSONObject
import java.io.File
import java.util.UUID

private const val PREFS_NAME = "ld_speaker_notes"
private const val PREF_DOCUMENTS = "speaker_note_documents_v1"

data class SpeakerNoteTemplate(
    val id: String,
    val title: String,
    val premise: String,
    val points: List<SpeakerNotePoint>,
    val tags: List<String>
)

data class SpeakerNoteDocument(
    val id: String,
    val sourceTemplateId: String,
    val title: String,
    val premise: String,
    val points: List<SpeakerNotePoint>,
    val tags: List<String>,
    val createdAt: Long,
    val updatedAt: Long
)

data class SpeakerNotePoint(
    val heading: String,
    val body: String,
    val subPoints: List<String>,
    val takeaways: List<String>,
    val powerLine: String,
    val writingSpace: String
)

data class SeedPack(
    val mode: String,
    val templates: List<SpeakerNoteTemplate>
)

private data class PointInputs(
    val heading: EditText,
    val body: EditText,
    val subPoints: EditText,
    val takeaways: EditText,
    val powerLine: EditText,
    val writingSpace: EditText
)

@Suppress("DEPRECATION")
class MainActivity : Activity() {
    private val ivory = Color.rgb(251, 247, 239)
    private val ink = Color.rgb(23, 19, 13)
    private val muted = Color.rgb(99, 89, 77)
    private val gold = Color.rgb(200, 168, 94)
    private val sand = Color.rgb(232, 216, 184)
    private val white = Color.WHITE

    private lateinit var webView: WebView
    private lateinit var contentFrame: FrameLayout
    private lateinit var notesView: ScrollView
    private lateinit var bottomNav: LinearLayout
    private lateinit var prefs: android.content.SharedPreferences

    private val documents = mutableListOf<SpeakerNoteDocument>()
    private val pointInputs = mutableListOf<PointInputs>()
    private var selectedDocumentId: String? = null
    private var selectedTab: String = "Home"
    private var titleInput: EditText? = null
    private var premiseInput: EditText? = null
    private var tagsInput: EditText? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        WebView.setWebContentsDebuggingEnabled(BuildConfig.DEBUG)

        prefs = getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
        loadDocuments()
        window.statusBarColor = ivory
        window.navigationBarColor = ivory

        val root = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            setBackgroundColor(ivory)
        }

        contentFrame = FrameLayout(this).apply {
            layoutParams = LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT,
                0,
                1f
            )
        }

        webView = createWebView()
        notesView = ScrollView(this).apply {
            visibility = View.GONE
            setBackgroundColor(ivory)
        }

        contentFrame.addView(webView)
        contentFrame.addView(notesView)
        bottomNav = LinearLayout(this).apply {
            orientation = LinearLayout.HORIZONTAL
            gravity = Gravity.CENTER
            setPadding(dp(8), dp(8), dp(8), dp(8))
            setBackgroundColor(white)
        }

        root.addView(contentFrame)
        root.addView(bottomNav)
        setContentView(root)

        renderNotesScreen()
        renderBottomNav()

        if (savedInstanceState == null) {
            loadWebRoute("/")
        } else {
            webView.restoreState(savedInstanceState)
            selectedTab = savedInstanceState.getString("selectedTab", "Home")
            setActiveSurface(selectedTab == "Notes")
            renderBottomNav()
        }
    }

    @Deprecated("Android framework deprecates this callback, but the no-AndroidX wrapper keeps this path explicit.")
    override fun onBackPressed() {
        if (selectedTab == "Notes") {
            saveActiveDocument()
            selectedTab = "Home"
            setActiveSurface(false)
            loadWebRoute("/")
            renderBottomNav()
            return
        }

        if (::webView.isInitialized && webView.canGoBack()) {
            webView.goBack()
        } else {
            super.onBackPressed()
        }
    }

    override fun onSaveInstanceState(outState: Bundle) {
        saveActiveDocument()
        outState.putString("selectedTab", selectedTab)
        if (::webView.isInitialized) {
            webView.saveState(outState)
        }
        super.onSaveInstanceState(outState)
    }

    private fun createWebView(): WebView {
        return WebView(this).apply {
            layoutParams = FrameLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT,
                ViewGroup.LayoutParams.MATCH_PARENT
            )
            setBackgroundColor(ivory)
            configureSettings(settings)
            webViewClient = object : WebViewClient() {
                override fun shouldOverrideUrlLoading(
                    view: WebView,
                    request: WebResourceRequest
                ): Boolean = handleUrl(request.url)
            }
        }
    }

    private fun configureSettings(settings: WebSettings) {
        settings.javaScriptEnabled = true
        settings.domStorageEnabled = true
        settings.databaseEnabled = true
        settings.loadWithOverviewMode = true
        settings.useWideViewPort = true
        settings.mediaPlaybackRequiresUserGesture = false
        settings.mixedContentMode = WebSettings.MIXED_CONTENT_COMPATIBILITY_MODE
    }

    private fun handleUrl(uri: Uri): Boolean {
        val scheme = uri.scheme?.lowercase()
        if (scheme == "http" || scheme == "https") {
            return !isInternalUrl(uri).also { internal ->
                if (!internal) openExternal(uri)
            }
        }

        openExternal(uri)
        return true
    }

    private fun isInternalUrl(uri: Uri): Boolean {
        val base = Uri.parse(BuildConfig.APP_URL)
        return uri.host.equals(base.host, ignoreCase = true)
    }

    private fun openExternal(uri: Uri) {
        try {
            startActivity(Intent(Intent.ACTION_VIEW, uri))
        } catch (_: ActivityNotFoundException) {
            Toast.makeText(this, "No app can open this link.", Toast.LENGTH_SHORT).show()
        }
    }

    private fun renderBottomNav() {
        bottomNav.removeAllViews()
        listOf("Home" to "/", "Speaking" to "/speaking", "Notes" to "", "Book" to "/book").forEach { item ->
            val label = item.first
            val route = item.second
            bottomNav.addView(navButton(label) {
                saveActiveDocument()
                selectedTab = label
                if (label == "Notes") {
                    setActiveSurface(true)
                    renderNotesScreen()
                } else {
                    setActiveSurface(false)
                    loadWebRoute(route)
                }
                renderBottomNav()
            })
        }
    }

    private fun navButton(label: String, action: () -> Unit): TextView {
        val active = selectedTab == label
        return TextView(this).apply {
            text = label
            gravity = Gravity.CENTER
            textSize = 13f
            typeface = Typeface.DEFAULT_BOLD
            setTextColor(if (active) ink else muted)
            setPadding(dp(8), dp(10), dp(8), dp(10))
            background = rounded(if (active) sand else white, if (active) gold else Color.TRANSPARENT)
            layoutParams = LinearLayout.LayoutParams(0, ViewGroup.LayoutParams.WRAP_CONTENT, 1f).apply {
                setMargins(dp(3), 0, dp(3), 0)
            }
            setOnClickListener { action() }
        }
    }

    private fun setActiveSurface(notes: Boolean) {
        webView.visibility = if (notes) View.GONE else View.VISIBLE
        notesView.visibility = if (notes) View.VISIBLE else View.GONE
    }

    private fun loadWebRoute(route: String) {
        webView.loadUrl(BuildConfig.APP_URL.trimEnd('/') + route)
    }

    private fun renderNotesScreen() {
        val container = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            setPadding(dp(18), dp(24), dp(18), dp(32))
            setBackgroundColor(ivory)
        }

        pointInputs.clear()
        val selected = selectedDocument() ?: newBlankDocument().also {
            documents.add(it)
            selectedDocumentId = it.id
            persistDocuments()
        }

        container.addView(kicker("Speaker Notes"))
        container.addView(titleText("Emergency notes, talk outlines, and final-race reminders."))
        container.addView(bodyText("Mode: ${BuildConfig.NOTES_MODE}. Notes stay on this device and work offline."))
        container.addView(actionRow(
            button("New Blank") {
                saveActiveDocument()
                val doc = newBlankDocument()
                documents.add(0, doc)
                selectedDocumentId = doc.id
                persistDocuments()
                renderNotesScreen()
            },
            button("Restore Templates") {
                saveActiveDocument()
                restoreTemplates()
                renderNotesScreen()
            }
        ))

        container.addView(notePicker())
        container.addView(editorFor(selected))
        notesView.removeAllViews()
        notesView.addView(container)
    }

    private fun notePicker(): View {
        val list = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            setPadding(0, dp(10), 0, dp(8))
        }
        documents.forEach { doc ->
            val row = TextView(this).apply {
                text = doc.title.ifBlank { "Untitled Speaker Notes" }
                textSize = 15f
                typeface = Typeface.DEFAULT_BOLD
                setTextColor(if (doc.id == selectedDocumentId) ink else muted)
                setPadding(dp(14), dp(12), dp(14), dp(12))
                background = rounded(if (doc.id == selectedDocumentId) white else Color.TRANSPARENT, sand)
                layoutParams = LinearLayout.LayoutParams(
                    ViewGroup.LayoutParams.MATCH_PARENT,
                    ViewGroup.LayoutParams.WRAP_CONTENT
                ).apply {
                    setMargins(0, dp(4), 0, dp(4))
                }
                setOnClickListener {
                    saveActiveDocument()
                    selectedDocumentId = doc.id
                    renderNotesScreen()
                }
            }
            list.addView(row)
        }
        return list
    }

    private fun editorFor(doc: SpeakerNoteDocument): View {
        val editor = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            setPadding(0, dp(10), 0, 0)
        }

        titleInput = input(doc.title, "Talk title", false)
        premiseInput = input(doc.premise, "One-line premise", true)
        tagsInput = input(doc.tags.joinToString(", "), "Tags", false)

        editor.addView(label("Talk Title"))
        editor.addView(requireNotNull(titleInput))
        editor.addView(label("One-Line Premise"))
        editor.addView(requireNotNull(premiseInput))
        editor.addView(label("Tags"))
        editor.addView(requireNotNull(tagsInput))

        doc.points.forEachIndexed { index, point ->
            editor.addView(sectionHeader("Main Point ${index + 1}"))
            val heading = input(point.heading, "Main point heading", false)
            val body = input(point.body, "Main point summary", true)
            val subPoints = input(point.subPoints.joinToString("\n"), "3 sub-points", true)
            val takeaways = input(point.takeaways.joinToString("\n"), "Key takeaways / life lessons learned", true)
            val powerLine = input(point.powerLine, "Power line", false)
            val writingSpace = input(point.writingSpace, "Writing space", true)

            editor.addView(label("Main Point"))
            editor.addView(heading)
            editor.addView(label("Point Summary"))
            editor.addView(body)
            editor.addView(label("3 Sub-Points"))
            editor.addView(subPoints)
            editor.addView(label("Key Takeaways / Life Lessons Learned"))
            editor.addView(takeaways)
            editor.addView(label("Power Line"))
            editor.addView(powerLine)
            editor.addView(label("Writing Space"))
            editor.addView(writingSpace)

            pointInputs.add(PointInputs(heading, body, subPoints, takeaways, powerLine, writingSpace))
        }

        editor.addView(actionRow(
            button("Save") {
                saveActiveDocument()
                Toast.makeText(this, "Notes saved.", Toast.LENGTH_SHORT).show()
                renderNotesScreen()
            },
            button("Duplicate") {
                saveActiveDocument()
                duplicateSelected()
                renderNotesScreen()
            }
        ))
        editor.addView(actionRow(
            button("Copy") {
                saveActiveDocument()
                copySelected()
            },
            button("Share") {
                saveActiveDocument()
                shareSelected()
            },
            button("PDF") {
                saveActiveDocument()
                sharePdfSelected()
            }
        ))
        editor.addView(actionRow(
            button("Delete") {
                deleteSelected()
                renderNotesScreen()
            }
        ))

        return editor
    }

    private fun saveActiveDocument() {
        val currentId = selectedDocumentId ?: return
        val existingIndex = documents.indexOfFirst { it.id == currentId }
        if (existingIndex < 0 || titleInput == null || premiseInput == null) return

        val updated = documents[existingIndex].copy(
            title = titleInput?.text?.toString()?.trim().orEmpty(),
            premise = premiseInput?.text?.toString()?.trim().orEmpty(),
            tags = tagsInput?.text?.toString().orEmpty().split(",").map { it.trim() }.filter { it.isNotBlank() },
            points = pointInputs.map { inputs ->
                SpeakerNotePoint(
                    heading = inputs.heading.text.toString().trim(),
                    body = inputs.body.text.toString().trim(),
                    subPoints = linesFrom(inputs.subPoints),
                    takeaways = linesFrom(inputs.takeaways),
                    powerLine = inputs.powerLine.text.toString().trim(),
                    writingSpace = inputs.writingSpace.text.toString().trim()
                )
            },
            updatedAt = System.currentTimeMillis()
        )
        documents[existingIndex] = updated
        persistDocuments()
    }

    private fun duplicateSelected() {
        val selected = selectedDocument() ?: return
        val now = System.currentTimeMillis()
        val copy = selected.copy(
            id = UUID.randomUUID().toString(),
            sourceTemplateId = selected.sourceTemplateId + "-copy-" + now,
            title = selected.title.ifBlank { "Untitled Speaker Notes" } + " Copy",
            createdAt = now,
            updatedAt = now
        )
        documents.add(0, copy)
        selectedDocumentId = copy.id
        persistDocuments()
    }

    private fun deleteSelected() {
        val currentId = selectedDocumentId ?: return
        documents.removeAll { it.id == currentId }
        if (documents.isEmpty()) {
            documents.add(newBlankDocument())
        }
        selectedDocumentId = documents.first().id
        persistDocuments()
    }

    private fun copySelected() {
        val selected = selectedDocument() ?: return
        val clipboard = getSystemService(Context.CLIPBOARD_SERVICE) as ClipboardManager
        clipboard.setPrimaryClip(ClipData.newPlainText(selected.title, formatDocument(selected)))
        Toast.makeText(this, "Notes copied.", Toast.LENGTH_SHORT).show()
    }

    private fun shareSelected() {
        val selected = selectedDocument() ?: return
        val intent = Intent(Intent.ACTION_SEND).apply {
            type = "text/plain"
            putExtra(Intent.EXTRA_SUBJECT, selected.title)
            putExtra(Intent.EXTRA_TEXT, formatDocument(selected))
        }
        startActivity(Intent.createChooser(intent, "Share speaker notes"))
    }

    private fun sharePdfSelected() {
        val selected = selectedDocument() ?: return
        val file = createPdf(selected)
        val uri = Uri.Builder()
            .scheme("content")
            .authority("${BuildConfig.APPLICATION_ID}.cachefiles")
            .appendPath(file.name)
            .build()
        val intent = Intent(Intent.ACTION_SEND).apply {
            type = "application/pdf"
            putExtra(Intent.EXTRA_STREAM, uri)
            addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
        }
        startActivity(Intent.createChooser(intent, "Share notes PDF"))
    }

    private fun createPdf(doc: SpeakerNoteDocument): File {
        val exportDir = File(cacheDir, "exports").apply { mkdirs() }
        val file = File(exportDir, safeFileName(doc.title.ifBlank { "speaker-notes" }) + ".pdf")
        val pdf = PdfDocument()
        val paint = Paint(Paint.ANTI_ALIAS_FLAG).apply {
            color = ink
            textSize = 12f
        }
        val titlePaint = Paint(Paint.ANTI_ALIAS_FLAG).apply {
            color = ink
            textSize = 18f
            typeface = Typeface.DEFAULT_BOLD
        }
        val width = 612
        val height = 792
        val margin = 42f
        var pageNumber = 1
        var page = pdf.startPage(PdfDocument.PageInfo.Builder(width, height, pageNumber).create())
        var canvas: Canvas = page.canvas
        var y = margin

        fun newPage() {
            pdf.finishPage(page)
            pageNumber += 1
            page = pdf.startPage(PdfDocument.PageInfo.Builder(width, height, pageNumber).create())
            canvas = page.canvas
            y = margin
        }

        fun drawWrapped(text: String, activePaint: Paint, lineHeight: Float) {
            val words = text.split(Regex("\\s+")).filter { it.isNotBlank() }
            var line = ""
            if (words.isEmpty()) {
                y += lineHeight
                return
            }
            words.forEach { word ->
                val test = if (line.isBlank()) word else "$line $word"
                if (activePaint.measureText(test) > width - margin * 2) {
                    if (y > height - margin) newPage()
                    canvas.drawText(line, margin, y, activePaint)
                    y += lineHeight
                    line = word
                } else {
                    line = test
                }
            }
            if (line.isNotBlank()) {
                if (y > height - margin) newPage()
                canvas.drawText(line, margin, y, activePaint)
                y += lineHeight
            }
        }

        drawWrapped(doc.title.ifBlank { "Speaker Notes" }, titlePaint, 24f)
        y += 10f
        formatDocument(doc).lines().forEach { line ->
            if (line.isBlank()) {
                y += 10f
            } else {
                drawWrapped(line, paint, 17f)
            }
        }
        pdf.finishPage(page)
        file.outputStream().use { pdf.writeTo(it) }
        pdf.close()
        return file
    }

    private fun selectedDocument(): SpeakerNoteDocument? {
        if (selectedDocumentId == null && documents.isNotEmpty()) {
            selectedDocumentId = documents.first().id
        }
        return documents.firstOrNull { it.id == selectedDocumentId } ?: documents.firstOrNull()
    }

    private fun loadDocuments() {
        val stored = prefs.getString(PREF_DOCUMENTS, null)
        val parsed = if (stored.isNullOrBlank()) emptyList() else parseDocuments(stored)
        documents.clear()
        documents.addAll(parsed.ifEmpty { seedDocuments() })
        selectedDocumentId = documents.firstOrNull()?.id
        persistDocuments()
    }

    private fun persistDocuments() {
        val array = JSONArray()
        documents.forEach { array.put(it.toJson()) }
        prefs.edit().putString(PREF_DOCUMENTS, array.toString()).apply()
    }

    private fun restoreTemplates() {
        val existingTemplateIds = documents.map { it.sourceTemplateId }.toSet()
        val restored = seedPack().templates
            .filterNot { existingTemplateIds.contains(it.id) }
            .map { it.toDocument() }
        if (restored.isEmpty()) {
            Toast.makeText(this, "Templates are already present.", Toast.LENGTH_SHORT).show()
            return
        }
        documents.addAll(0, restored)
        selectedDocumentId = restored.first().id
        persistDocuments()
        Toast.makeText(this, "Templates restored.", Toast.LENGTH_SHORT).show()
    }

    private fun parseDocuments(raw: String): List<SpeakerNoteDocument> {
        return try {
            val array = JSONArray(raw)
            List(array.length()) { index -> array.getJSONObject(index).toDocument() }
        } catch (_: Exception) {
            emptyList()
        }
    }

    private fun seedDocuments(): List<SpeakerNoteDocument> {
        return seedPack().templates.map { it.toDocument() }
    }

    private fun seedPack(): SeedPack {
        return if (BuildConfig.NOTES_MODE == "public-blank") {
            SeedPack("public-blank", blankTemplates())
        } else {
            SeedPack("private-seeded", privateTemplates())
        }
    }

    private fun privateTemplates(): List<SpeakerNoteTemplate> = listOf(
        SpeakerNoteTemplate(
            id = "road-to-the-olympics",
            title = "Road to the Olympics",
            premise = "The road began long before the medals, and every season built discipline, courage, faith, and legacy.",
            tags = listOf("Olympics", "faith", "legacy", "resilience"),
            points = listOf(
                SpeakerNotePoint(
                    heading = "The Foundation Was Built Before The Medals",
                    body = "The road to the Olympics began on the island, where daily life built discipline before the world ever saw the athlete.",
                    subPoints = listOf(
                        "Jamaica was the first training ground: walking, racing, soccer, school, chores, church, family, beach, waterfalls, and mountains.",
                        "Daily routines built endurance, responsibility, respect, faith, identity, and community connection.",
                        "Family, friends, elders, faith, and community poured in strength before medals, titles, or public recognition."
                    ),
                    takeaways = listOf(
                        "Do not despise small beginnings; ordinary routines can build extraordinary strength.",
                        "A strong foundation travels with you into every new season.",
                        "Before success becomes public, preparation is often hidden."
                    ),
                    powerLine = "Finish with faith. Finish with courage. Finish with peace.",
                    writingSpace = "Add memories, scriptures, examples, audience ideas, or stories."
                ),
                SpeakerNotePoint(
                    heading = "The New Country Became A New Place To Grow",
                    body = "Moving to Edmonton at age 10 did not erase the foundation; it expanded the story through school, sports, music, and leadership.",
                    subPoints = listOf(
                        "New country, new school, new teachers, new students, and a new community became part of the support system.",
                        "Teachers became elders, students became friends, and snow became a place to imagine white sandy beach.",
                        "Growth came through volleyball, basketball, gymnastics, track and field, floor hockey, school band, leadership, and coaching."
                    ),
                    takeaways = listOf(
                        "Starting over does not mean starting empty; you carry your foundation with you.",
                        "Trying many activities can reveal gifts, confidence, teamwork, leadership, and purpose.",
                        "Excellence grows when discipline, support, opportunity, and courage work together."
                    ),
                    powerLine = "Finish with faith. Finish with courage. Finish with peace.",
                    writingSpace = "Add memories, scriptures, examples, audience ideas, or stories."
                ),
                SpeakerNotePoint(
                    heading = "Finish The Race And Pour Into Others",
                    body = "The Olympic year brought injury and pain, but crossing the finish line created peace and became the lesson that now fuels legacy.",
                    subPoints = listOf(
                        "Before the 1988 Olympic Trials, a broken bone in the foot threatened the dream, but the decision was made to still compete.",
                        "Running both sprint races was not only about winning; it was about crossing the line and living without regret.",
                        "After athletics, the mission became training youth and pouring into them what family, elders, teachers, coaches, and faith had poured in."
                    ),
                    takeaways = listOf(
                        "Pain may change how the race looks, but it does not have to cancel the purpose.",
                        "Sometimes the greatest victory is finishing with peace, not standing on the podium.",
                        "Legacy is taking what strengthened you and using it to strengthen the next generation."
                    ),
                    powerLine = "Finish with faith. Finish with courage. Finish with peace.",
                    writingSpace = "Add memories, scriptures, examples, audience ideas, or stories."
                )
            )
        ),
        SpeakerNoteTemplate(
            id = "finish-your-race",
            title = "Finish Your Race",
            premise = "Pain, betrayal, and recovery can become purpose when the assignment is finished with courage and peace.",
            tags = listOf("finish", "resilience", "purpose", "faith"),
            points = listOf(
                SpeakerNotePoint(
                    heading = "Finish Even When Life Hurts",
                    body = "The Olympic Trials became more than a race. With a broken foot and years of training behind her, the decision was to show up, run, and finish with peace.",
                    subPoints = listOf(
                        "Trained for over 20 years as a sprinter, earning city, provincial, and national success.",
                        "Broke a bone in the foot just weeks before the Olympic Trials and faced a painful decision.",
                        "Ran both races in pain to cross the finish line and avoid living with regret or torment."
                    ),
                    takeaways = listOf(
                        "Victory is not always the podium; sometimes victory is finishing what pain tried to stop.",
                        "Do not let injury, fear, or disappointment make the final decision for your life.",
                        "Finish so your future self can say, I showed up. I gave my best. I did not quit."
                    ),
                    powerLine = "The finish line is not just a place; it is peace.",
                    writingSpace = "Add memories, scriptures, examples, audience ideas, or stories."
                ),
                SpeakerNotePoint(
                    heading = "Rebuild After Setbacks And Betrayal",
                    body = "After sports, the business vision faced divorce, young children, hard timing, and betrayal, but the purpose to serve youth and family did not die.",
                    subPoints = listOf(
                        "Started a business vision while facing divorce, young children, pressure, and hard timing.",
                        "Experienced people moving forward with the vision without her, but refused to become bitter or stop.",
                        "Continued coaching youth, serving the community, and helping her children rise into higher education."
                    ),
                    takeaways = listOf(
                        "People can copy an idea, but they cannot copy your story, your purpose, or your calling.",
                        "A setback does not mean stop; betrayal can become wisdom, strategy, and discernment.",
                        "Real leadership is building again and helping others win while you are still healing."
                    ),
                    powerLine = "People may have opinions, but they do not have your assignment.",
                    writingSpace = "Add memories, scriptures, examples, audience ideas, or stories."
                ),
                SpeakerNotePoint(
                    heading = "Turn Pain Into Purpose",
                    body = "A serious vehicle accident and partial paralysis forced a surrender of the old plan, but recovery opened a new way to impact lives online and around the world.",
                    subPoints = listOf(
                        "A serious vehicle accident caused partial paralysis, many injuries, and a season of recovery.",
                        "On the bed of recovery, surrender led to books, programs, online meetings, and blogs.",
                        "Now the third business is being built online with her children to impact lives locally and globally."
                    ),
                    takeaways = listOf(
                        "Your painful chapter is not the end; it may be the beginning of a greater assignment.",
                        "Do not confuse delay with denial or a setback with a full stop.",
                        "Finish the healing, finish the dream, finish the assignment, and finish your race."
                    ),
                    powerLine = "What you survive can become what you use to change the world.",
                    writingSpace = "Add memories, scriptures, examples, audience ideas, or stories."
                )
            )
        )
    )

    private fun blankTemplates(): List<SpeakerNoteTemplate> = listOf(
        blankTemplate("road-to-the-olympics-template", "Road to the Olympics Template"),
        blankTemplate("finish-your-race-template", "Finish Your Race Template")
    )

    private fun blankTemplate(id: String, title: String): SpeakerNoteTemplate {
        return SpeakerNoteTemplate(
            id = id,
            title = title,
            premise = "",
            tags = listOf("template"),
            points = List(3) { index ->
                SpeakerNotePoint(
                    heading = "Main Point ${index + 1}",
                    body = "",
                    subPoints = listOf("", "", ""),
                    takeaways = listOf("", "", ""),
                    powerLine = "",
                    writingSpace = ""
                )
            }
        )
    }

    private fun newBlankDocument(): SpeakerNoteDocument {
        val now = System.currentTimeMillis()
        return blankTemplate("custom-" + UUID.randomUUID(), "Emergency Speaker Notes").toDocument(now)
    }

    private fun SpeakerNoteTemplate.toDocument(now: Long = System.currentTimeMillis()): SpeakerNoteDocument {
        return SpeakerNoteDocument(
            id = UUID.randomUUID().toString(),
            sourceTemplateId = id,
            title = title,
            premise = premise,
            points = points,
            tags = tags,
            createdAt = now,
            updatedAt = now
        )
    }

    private fun SpeakerNoteDocument.toJson(): JSONObject {
        return JSONObject()
            .put("id", id)
            .put("sourceTemplateId", sourceTemplateId)
            .put("title", title)
            .put("premise", premise)
            .put("tags", JSONArray(tags))
            .put("createdAt", createdAt)
            .put("updatedAt", updatedAt)
            .put("points", JSONArray().also { array ->
                points.forEach { point ->
                    array.put(
                        JSONObject()
                            .put("heading", point.heading)
                            .put("body", point.body)
                            .put("subPoints", JSONArray(point.subPoints))
                            .put("takeaways", JSONArray(point.takeaways))
                            .put("powerLine", point.powerLine)
                            .put("writingSpace", point.writingSpace)
                    )
                }
            })
    }

    private fun JSONObject.toDocument(): SpeakerNoteDocument {
        val now = System.currentTimeMillis()
        val pointsArray = optJSONArray("points") ?: JSONArray()
        return SpeakerNoteDocument(
            id = optString("id", UUID.randomUUID().toString()),
            sourceTemplateId = optString("sourceTemplateId", "imported"),
            title = optString("title", ""),
            premise = optString("premise", ""),
            tags = optJSONArray("tags").toStringList(),
            createdAt = optLong("createdAt", now),
            updatedAt = optLong("updatedAt", now),
            points = List(pointsArray.length()) { index ->
                val point = pointsArray.getJSONObject(index)
                SpeakerNotePoint(
                    heading = point.optString("heading", ""),
                    body = point.optString("body", ""),
                    subPoints = point.optJSONArray("subPoints").toStringList(),
                    takeaways = point.optJSONArray("takeaways").toStringList(),
                    powerLine = point.optString("powerLine", ""),
                    writingSpace = point.optString("writingSpace", "")
                )
            }.ifEmpty { blankTemplate("imported-template", "Imported Template").points }
        )
    }

    private fun formatDocument(doc: SpeakerNoteDocument): String {
        val builder = StringBuilder()
        builder.appendLine(doc.title.ifBlank { "Speaker Notes" })
        if (doc.premise.isNotBlank()) builder.appendLine(doc.premise)
        if (doc.tags.isNotEmpty()) builder.appendLine("Tags: ${doc.tags.joinToString(", ")}")
        builder.appendLine()
        doc.points.forEachIndexed { index, point ->
            builder.appendLine("MAIN POINT ${index + 1}")
            builder.appendLine(point.heading)
            if (point.body.isNotBlank()) builder.appendLine(point.body)
            builder.appendLine()
            builder.appendLine("3 SUB-POINTS")
            point.subPoints.filter { it.isNotBlank() }.forEach { builder.appendLine("- $it") }
            builder.appendLine()
            builder.appendLine("KEY TAKEAWAYS / LIFE LESSONS LEARNED")
            point.takeaways.filter { it.isNotBlank() }.forEach { builder.appendLine("- $it") }
            builder.appendLine()
            builder.appendLine("POWER LINE")
            builder.appendLine(point.powerLine)
            builder.appendLine()
            builder.appendLine("WRITING SPACE")
            builder.appendLine(point.writingSpace)
            builder.appendLine()
        }
        return builder.toString().trim()
    }

    private fun linesFrom(input: EditText): List<String> {
        return input.text.toString().lines().map { it.trim() }.filter { it.isNotBlank() }
    }

    private fun safeFileName(value: String): String {
        return value.lowercase()
            .replace(Regex("[^a-z0-9]+"), "-")
            .trim('-')
            .ifBlank { "speaker-notes" }
    }

    private fun input(value: String, hintText: String, multiline: Boolean): EditText {
        return EditText(this).apply {
            setText(value)
            hint = hintText
            textSize = 16f
            setTextColor(ink)
            setHintTextColor(Color.rgb(144, 132, 112))
            setPadding(dp(12), dp(10), dp(12), dp(10))
            background = rounded(white, sand)
            minLines = if (multiline) 3 else 1
            maxLines = if (multiline) 8 else 1
            inputType = if (multiline) {
                InputType.TYPE_CLASS_TEXT or InputType.TYPE_TEXT_FLAG_MULTI_LINE or InputType.TYPE_TEXT_FLAG_CAP_SENTENCES
            } else {
                InputType.TYPE_CLASS_TEXT or InputType.TYPE_TEXT_FLAG_CAP_SENTENCES
            }
            layoutParams = LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT,
                ViewGroup.LayoutParams.WRAP_CONTENT
            ).apply {
                setMargins(0, dp(4), 0, dp(12))
            }
        }
    }

    private fun button(textValue: String, action: () -> Unit): Button {
        return Button(this).apply {
            text = textValue
            textSize = 13f
            isAllCaps = false
            setTextColor(ink)
            background = rounded(white, gold)
            setPadding(dp(8), dp(8), dp(8), dp(8))
            layoutParams = LinearLayout.LayoutParams(0, ViewGroup.LayoutParams.WRAP_CONTENT, 1f).apply {
                setMargins(dp(3), dp(4), dp(3), dp(4))
            }
            setOnClickListener { action() }
        }
    }

    private fun actionRow(vararg buttons: Button): View {
        return LinearLayout(this).apply {
            orientation = LinearLayout.HORIZONTAL
            buttons.forEach { addView(it) }
        }
    }

    private fun kicker(value: String): TextView {
        return TextView(this).apply {
            text = value.uppercase()
            textSize = 12f
            typeface = Typeface.DEFAULT_BOLD
            setTextColor(gold)
            setPadding(0, 0, 0, dp(6))
        }
    }

    private fun titleText(value: String): TextView {
        return TextView(this).apply {
            text = value
            textSize = 30f
            typeface = Typeface.create(Typeface.SERIF, Typeface.BOLD)
            setTextColor(ink)
            setPadding(0, 0, 0, dp(8))
        }
    }

    private fun bodyText(value: String): TextView {
        return TextView(this).apply {
            text = value
            textSize = 15f
            setTextColor(muted)
            setPadding(0, 0, 0, dp(12))
        }
    }

    private fun label(value: String): TextView {
        return TextView(this).apply {
            text = value
            textSize = 12f
            typeface = Typeface.DEFAULT_BOLD
            setTextColor(muted)
            setPadding(0, dp(6), 0, 0)
        }
    }

    private fun sectionHeader(value: String): TextView {
        return TextView(this).apply {
            text = value
            textSize = 18f
            typeface = Typeface.DEFAULT_BOLD
            setTextColor(ink)
            setPadding(0, dp(18), 0, dp(6))
        }
    }

    private fun rounded(fillColor: Int, strokeColor: Int): android.graphics.drawable.GradientDrawable {
        return android.graphics.drawable.GradientDrawable().apply {
            color = android.content.res.ColorStateList.valueOf(fillColor)
            cornerRadius = dp(8).toFloat()
            if (strokeColor != Color.TRANSPARENT) setStroke(dp(1), strokeColor)
        }
    }

    private fun dp(value: Int): Int = (value * resources.displayMetrics.density).toInt()
}

private fun JSONArray?.toStringList(): List<String> {
    if (this == null) return emptyList()
    return List(length()) { index -> optString(index) }
}

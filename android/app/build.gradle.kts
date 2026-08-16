plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}

val ldAppUrlProvider = providers.gradleProperty("LD_APP_URL")
    .orElse(providers.environmentVariable("LD_APP_URL"))
    .orElse("http://10.0.2.2:3000")

val escapedLdAppUrl = ldAppUrlProvider.get()
    .replace("\\", "\\\\")
    .replace("\"", "\\\"")

val requestedNotesModeProvider = providers.gradleProperty("LD_NOTES_MODE")
    .orElse(providers.environmentVariable("LD_NOTES_MODE"))
    .orElse("private-seeded")

fun validateNotesMode(value: String): String {
    if (value != "private-seeded" && value != "public-blank") {
        throw GradleException("LD_NOTES_MODE must be private-seeded or public-blank.")
    }
    return value
}

android {
    namespace = "com.lornettedaye.speaker"
    compileSdk = 35

    defaultConfig {
        applicationId = "com.lornettedaye.speaker"
        minSdk = 26
        targetSdk = 35
        versionCode = 1
        versionName = "1.0.0"

        buildConfigField("String", "PRODUCT_NAME", "\"LD Speaker\"")
        buildConfigField("String", "APP_URL", "\"$escapedLdAppUrl\"")
    }

    flavorDimensions += "notesMode"

    productFlavors {
        create("privateSeeded") {
            dimension = "notesMode"
            applicationIdSuffix = ".private"
            versionNameSuffix = "-private"
            resValue("string", "app_name", "LD Speaker Private")
            buildConfigField("String", "NOTES_MODE", "\"private-seeded\"")
        }
        create("publicBlank") {
            dimension = "notesMode"
            resValue("string", "app_name", "LD Speaker")
            buildConfigField("String", "NOTES_MODE", "\"public-blank\"")
        }
    }

    buildFeatures {
        buildConfig = true
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }

    kotlinOptions {
        jvmTarget = "17"
    }
}

tasks.register("assembleLdSpeakerDebug") {
    val notesMode = validateNotesMode(requestedNotesModeProvider.get())
    dependsOn(if (notesMode == "public-blank") "assemblePublicBlankDebug" else "assemblePrivateSeededDebug")
}

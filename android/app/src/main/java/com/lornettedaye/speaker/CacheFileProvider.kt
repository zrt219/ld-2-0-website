package com.lornettedaye.speaker

import android.content.ContentProvider
import android.content.ContentValues
import android.database.Cursor
import android.net.Uri
import android.os.ParcelFileDescriptor
import java.io.File

class CacheFileProvider : ContentProvider() {
    override fun onCreate(): Boolean = true

    override fun getType(uri: Uri): String = when {
        uri.lastPathSegment?.endsWith(".pdf", ignoreCase = true) == true -> "application/pdf"
        else -> "application/octet-stream"
    }

    override fun openFile(uri: Uri, mode: String): ParcelFileDescriptor {
        val fileName = uri.lastPathSegment ?: throw IllegalArgumentException("Missing file name")
        val exportDir = File(requireNotNull(context).cacheDir, "exports")
        val file = File(exportDir, fileName).canonicalFile
        val exportRoot = exportDir.canonicalFile

        if (!file.path.startsWith(exportRoot.path) || !file.isFile) {
            throw IllegalArgumentException("Unknown exported file")
        }

        return ParcelFileDescriptor.open(file, ParcelFileDescriptor.MODE_READ_ONLY)
    }

    override fun query(
        uri: Uri,
        projection: Array<out String>?,
        selection: String?,
        selectionArgs: Array<out String>?,
        sortOrder: String?
    ): Cursor? = null

    override fun insert(uri: Uri, values: ContentValues?): Uri? = null

    override fun delete(uri: Uri, selection: String?, selectionArgs: Array<out String>?): Int = 0

    override fun update(
        uri: Uri,
        values: ContentValues?,
        selection: String?,
        selectionArgs: Array<out String>?
    ): Int = 0
}

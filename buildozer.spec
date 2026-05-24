[app]

title = Kivy Test App

package.name = kivytest
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy==2.3.0

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

android.api = 34
android.minapi = 21

# İkon ve presplash (opsiyonel - yoksa hata verebilir, silebilirsin)
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/presplash.png

[buildozer]
log_level = 2

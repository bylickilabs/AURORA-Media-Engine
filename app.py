import os
import webbrowser
import tkinter as tk
from tkinter import filedialog, messagebox

import customtkinter as ctk
import vlc

APP_NAME = "AURORA Media Engine"
APP_VERSION = "1.0.0"
APP_COMPANY = "©Thorsten Bylicki | ©BYLICKILABS"
APP_WEBSITE = "https://www.bylickilabs.de"
APP_SUPPORT_EMAIL = "bylicki@mail.de"
APP_GITHUB = "https://github.com/bylickilabs"

LANG = "de"

I18N = {
    "de": {
        "open_video": "Video öffnen",
        "open_subtitle": "Untertitel öffnen",
        "play_pause": "Play/Pause",
        "stop": "Stop",
        "volume": "Lautstärke",
        "status_no_video": "Kein Video geladen",
        "status_video": "Aktives Video: {name}",
        "time_default": "00:00 / 00:00",
        "info_title": "Über diese Anwendung",
        "info_body": (
            "{app_name}\n"
            "Version {app_version}\n"
            "Entwickler: {company}\n\n"
            "Diese Anwendung wurde entwickelt, um lokale Medieninhalte "
            "(MP4, MKV) mit SRT-Untertiteln stabil und komfortabel "
            "abzuspielen.\n\n"
            "Funktionen:\n"
            "• Unterstützung für MP4 & MKV\n"
            "• SRT-Untertitel\n"
            "• Sprachumschaltung (Deutsch / Englisch)\n"
            "• Lautstärkeregelung und Spulen (Seekbar)\n"
            "• GitHub-Integration\n"
        ),
        "dialog_no_video_title": "Kein Video",
        "dialog_no_video_message": "Bitte zuerst ein Video auswählen.",
        "btn_github": "GitHub",
        "btn_info": "Info",
        "link_website": "Webseite",
        "link_support": "Support",
        "link_github": "GitHub",
        "ok_button": "Schließen",
    },
    "en": {
        "open_video": "Open Video",
        "open_subtitle": "Open Subtitle",
        "play_pause": "Play/Pause",
        "stop": "Stop",
        "volume": "Volume",
        "status_no_video": "No video loaded",
        "status_video": "Active video: {name}",
        "time_default": "00:00 / 00:00",
        "info_title": "About this Application",
        "info_body": (
            "{app_name}\n"
            "Version {app_version}\n"
            "Developer: {company}\n\n"
            "This application is designed to play local media content "
            "(MP4, MKV) with SRT subtitles in a stable and convenient way.\n\n"
            "Features:\n"
            "• Support for MP4 & MKV\n"
            "• SRT subtitles\n"
            "• Language switch (German / English)\n"
            "• Volume control and seeking (seekbar)\n"
            "• GitHub integration\n"
        ),
        "dialog_no_video_title": "No video",
        "dialog_no_video_message": "Please select a video first.",
        "btn_github": "GitHub",
        "btn_info": "Info",
        "link_website": "Website",
        "link_support": "Support",
        "link_github": "GitHub",
        "ok_button": "Close",
    },
}

class MediaPlayerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title(f"{APP_NAME} — v{APP_VERSION}")
        self.geometry("1000x600")
        self.minsize(800, 450)

        self.vlc_instance = vlc.Instance("--no-osd", "--no-video-title-show", "--no-overlay", "--no-fullscreen", "--video-wallpaper", "--verbose=-1", "--quiet")
        self.player = self.vlc_instance.media_player_new()
        self.video_path: str | None = None
        self.subtitle_path: str | None = None
        self.is_fullscreen = False
        self.prev_geometry: str | None = None
        self.top_frame = None
        self.status_frame = None
        self.controls_frame = None
        self.btn_open_video = None
        self.btn_open_subtitle = None
        self.btn_play_pause = None
        self.btn_stop = None
        self.lbl_volume = None
        self.lbl_status = None
        self.lbl_time = None
        self.seek_slider = None
        self.volume_slider = None
        self.btn_de = None
        self.btn_en = None
        self.btn_github = None
        self.btn_info = None
        self.logo_image = None
        self.video_frame = None
        self._build_ui()
        
        self.bind("<Escape>", lambda e: self.exit_fullscreen())
        self.bind("<F>", lambda e: self.toggle_fullscreen())

        self._update_playback_loop()

    def _build_ui(self):
        global LANG
        lang_dict = I18N[LANG]

        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.pack(fill="x", padx=10, pady=(10, 5))

        self._load_logo(self.top_frame)

        self.btn_open_video = ctk.CTkButton(
            self.top_frame,
            text=lang_dict["open_video"],
            command=self.open_video,
        )
        self.btn_open_video.pack(side="left", padx=5)

        self.btn_open_subtitle = ctk.CTkButton(
            self.top_frame,
            text=lang_dict["open_subtitle"],
            command=self.open_subtitle,
        )
        self.btn_open_subtitle.pack(side="left", padx=5)

        self.btn_github = ctk.CTkButton(
            self.top_frame,
            text=lang_dict["btn_github"],
            command=lambda: webbrowser.open(APP_GITHUB),
        )
        self.btn_github.pack(side="left", padx=5)

        spacer = ctk.CTkLabel(self.top_frame, text="")
        spacer.pack(side="left", expand=True)

        lang_frame = ctk.CTkFrame(self.top_frame)
        lang_frame.pack(side="right", padx=5)

        self.btn_de = ctk.CTkButton(
            lang_frame,
            text="DE",
            width=40,
            command=lambda: self.set_language("de"),
        )
        self.btn_de.pack(side="left", padx=2)

        self.btn_en = ctk.CTkButton(
            lang_frame,
            text="EN",
            width=40,
            command=lambda: self.set_language("en"),
        )
        self.btn_en.pack(side="left", padx=2)

        self.btn_info = ctk.CTkButton(
            self.top_frame,
            text=lang_dict["btn_info"],
            width=70,
            command=self.show_info,
        )
        self.btn_info.pack(side="right", padx=5)

        self.status_frame = ctk.CTkFrame(self)
        self.status_frame.pack(fill="x", padx=10, pady=(0, 5))

        self.lbl_status = ctk.CTkLabel(
            self.status_frame,
            text=lang_dict["status_no_video"],
            anchor="w",
        )
        self.lbl_status.pack(fill="x", padx=5)

        self.video_frame = ctk.CTkFrame(self, corner_radius=12)
        self.video_frame.pack(expand=True, fill="both", padx=10, pady=5)

        self.video_frame.bind("<Double-Button-1>", lambda e: self.toggle_fullscreen())

        self.controls_frame = ctk.CTkFrame(self)
        self.controls_frame.pack(fill="x", padx=10, pady=(5, 10))

        self.btn_play_pause = ctk.CTkButton(
            self.controls_frame,
            text=lang_dict["play_pause"],
            width=100,
            command=self.toggle_play_pause,
        )
        self.btn_play_pause.pack(side="left", padx=5)

        self.btn_stop = ctk.CTkButton(
            self.controls_frame,
            text=lang_dict["stop"],
            width=80,
            command=self.stop,
        )
        self.btn_stop.pack(side="left", padx=5)

        self.lbl_time = ctk.CTkLabel(self.controls_frame, text=lang_dict["time_default"])
        self.lbl_time.pack(side="left", padx=10)

        self.seek_slider = ctk.CTkSlider(
            self.controls_frame,
            from_=0,
            to=100,
            number_of_steps=1000,
            command=self.on_seek,
        )
        self.seek_slider.pack(side="left", fill="x", expand=True, padx=10)

        self.lbl_volume = ctk.CTkLabel(self.controls_frame, text=lang_dict["volume"])
        self.lbl_volume.pack(side="left", padx=(5, 0))

        self.volume_slider = ctk.CTkSlider(
            self.controls_frame,
            from_=0,
            to=100,
            number_of_steps=100,
            command=self.set_volume,
        )
        self.volume_slider.set(80)
        self.volume_slider.pack(side="left", padx=5)

        self.player.audio_set_volume(80)

        self._update_language_ui()

    def _load_logo(self, parent_frame: ctk.CTkFrame):
        """Logo aus assets/app_icon.png laden und links anzeigen."""
        try:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            icon_path = os.path.join(base_dir, "assets", "app_icon.png")
            if os.path.exists(icon_path):
                self.logo_image = tk.PhotoImage(file=icon_path)
                logo_label = ctk.CTkLabel(parent_frame, image=self.logo_image, text="")
                logo_label.pack(side="left", padx=(5, 10))
            else:
                logo_label = ctk.CTkLabel(parent_frame, text=APP_NAME)
                logo_label.pack(side="left", padx=(5, 10))
        except Exception:
            logo_label = ctk.CTkLabel(parent_frame, text=APP_NAME)
            logo_label.pack(side="left", padx=(5, 10))

    def set_language(self, lang: str):
        """Sprache auf 'de' oder 'en' setzen, UI live aktualisieren."""
        global LANG
        if lang not in I18N:
            return
        if LANG == lang:
            return
        LANG = lang
        self._update_language_ui()

    def _update_language_ui(self):
        """Sämtliche UI-Texte und Sprach-Buttons aktualisieren."""
        lang_dict = I18N[LANG]

        self.title(f"{APP_NAME} — v{APP_VERSION}")

        if self.btn_open_video:
            self.btn_open_video.configure(text=lang_dict["open_video"])
        if self.btn_open_subtitle:
            self.btn_open_subtitle.configure(text=lang_dict["open_subtitle"])
        if self.btn_play_pause:
            self.btn_play_pause.configure(text=lang_dict["play_pause"])
        if self.btn_stop:
            self.btn_stop.configure(text=lang_dict["stop"])
        if self.lbl_volume:
            self.lbl_volume.configure(text=lang_dict["volume"])
        if self.btn_github:
            self.btn_github.configure(text=lang_dict["btn_github"])
        if self.btn_info:
            self.btn_info.configure(text=lang_dict["btn_info"])

        if self.lbl_status:
            if self.video_path:
                name = os.path.basename(self.video_path) if self.video_path else ""
                self.lbl_status.configure(
                    text=lang_dict["status_video"].format(name=name)
                )
            else:
                self.lbl_status.configure(text=lang_dict["status_no_video"])

        if self.lbl_time and self.player.get_length() <= 0:
            self.lbl_time.configure(text=lang_dict["time_default"])

        if self.btn_de and self.btn_en:
            if LANG == "de":
                self.btn_de.configure(fg_color="dodgerblue")
                self.btn_en.configure(fg_color="gray25")
            else:
                self.btn_en.configure(fg_color="dodgerblue")
                self.btn_de.configure(fg_color="gray25")

    def _bind_vlc(self, frame):
        """VLC-Videoausgabe an ein Frame binden."""
        frame.update_idletasks()
        try:
            self.player.set_hwnd(frame.winfo_id())
        except Exception:
            pass

    def toggle_fullscreen(self):
        """Vollbildmodus – nur Videoframe, ohne Fensterrahmen."""
        if not self.is_fullscreen:
            self.is_fullscreen = True
            self.prev_geometry = self.geometry()

            if self.top_frame: self.top_frame.pack_forget()
            if self.status_frame: self.status_frame.pack_forget()
            if self.controls_frame: self.controls_frame.pack_forget()

            self.attributes("-fullscreen", True)

            self._bind_vlc(self.video_frame)
            self.after(200, lambda: self._bind_vlc(self.video_frame))

        else:
            self.exit_fullscreen()

    def exit_fullscreen(self):
        """Zurück aus Vollbild – UI wiederherstellen."""
        self.is_fullscreen = False
        self.attributes("-fullscreen", False)

        if self.prev_geometry:
            self.geometry(self.prev_geometry)

        if self.top_frame:
            self.top_frame.pack(fill="x", padx=10, pady=(10, 5))
        if self.status_frame:
            self.status_frame.pack(fill="x", padx=10, pady=(0, 5))
        if self.controls_frame:
            self.controls_frame.pack(fill="x", padx=10, pady=(5, 10))

        self._bind_vlc(self.video_frame)
        self.after(200, lambda: self._bind_vlc(self.video_frame))


    def exit_fullscreen(self):
        """Sicher aus Vollbild zurückkehren und UI wieder einblenden."""
        self.is_fullscreen = False
        self.overrideredirect(False)
        self.attributes("-fullscreen", False)

        if self.top_frame:
            self.top_frame.pack(fill="x", padx=10, pady=(10, 5))
        if self.status_frame:
            self.status_frame.pack(fill="x", padx=10, pady=(0, 5))
        if self.controls_frame:
            self.controls_frame.pack(fill="x", padx=10, pady=(5, 10))

        if self.prev_geometry:
            self.geometry(self.prev_geometry)

        self._bind_vlc(self.video_frame)
        self.after(200, lambda: self._bind_vlc(self.video_frame))

    def _bind_vlc(self, frame):
        frame.update_idletasks()
        try:
            self.player.set_hwnd(frame.winfo_id())
            self.player.video_set_scale(0)
            self.player.video_set_aspect_ratio("16:9")
        except Exception:
            pass

    def _prepare_media(self):
        """Media-Objekt (Video + Untertitel) vorbereiten und an das Video-Frame binden."""

    def _prepare_media(self):
        """Media-Objekt (Video + Untertitel) vorbereiten und an das Video-Frame binden."""
        if not self.video_path:
            return

        media = self.vlc_instance.media_new(self.video_path)

        if self.subtitle_path:
            media.add_option(f"sub-file={self.subtitle_path}")

        self.player.stop()
        self.player.set_media(media)

        self._bind_vlc(self.video_frame)

        if self.volume_slider:
            self.player.audio_set_volume(int(self.volume_slider.get()))

    def open_video(self):
        filetypes = [
            ("Video-Dateien", "*.mp4 *.mkv *.avi *.mov"),
            ("Alle Dateien", "*.*"),
        ]
        path = filedialog.askopenfilename(
            title=I18N[LANG]["open_video"],
            filetypes=filetypes,
        )
        if not path:
            return

        self.video_path = path
        self._prepare_media()
        self._update_language_ui()

    def open_subtitle(self):
        filetypes = [
            ("SRT Untertitel", "*.srt"),
            ("Alle Dateien", "*.*"),
        ]
        title = I18N[LANG]["open_subtitle"]
        path = filedialog.askopenfilename(
            title=title,
            filetypes=filetypes,
        )
        if not path:
            return

        self.subtitle_path = path
        self._prepare_media()

    def toggle_play_pause(self):
        if not self.video_path:
            lang_dict = I18N[LANG]
            messagebox.showwarning(
                lang_dict["dialog_no_video_title"],
                lang_dict["dialog_no_video_message"],
            )
            return

        state = self.player.get_state()
        if state in (vlc.State.NothingSpecial, vlc.State.Stopped, vlc.State.Ended):
            self._prepare_media()
            self.player.play()
        else:
            if self.player.is_playing():
                self.player.pause()
            else:
                self.player.play()

    def stop(self):
        self.player.stop()

    def set_volume(self, value):
        try:
            vol = int(float(value))
        except ValueError:
            vol = 80
        self.player.audio_set_volume(vol)

    def on_seek(self, value):
        try:
            pos = float(value) / 100.0
        except ValueError:
            pos = 0.0

        if self.player.get_length() > 0:
            self.player.set_position(pos)

    def _format_time(self, ms: int) -> str:
        if ms <= 0:
            return "00:00"
        seconds = ms // 1000
        m = seconds // 60
        s = seconds % 60
        return f"{m:02d}:{s:02d}"

    def _update_playback_loop(self):
        """Seekbar & Zeitlabel regelmäßig aktualisieren."""
        try:
            length = self.player.get_length()
            lang_dict = I18N[LANG]

            if length > 0:
                pos = self.player.get_position()
                current_ms = int(length * pos)

                if self.seek_slider:
                    self.seek_slider.set(pos * 100.0)

                if self.lbl_time:
                    current_str = self._format_time(current_ms)
                    total_str = self._format_time(length)
                    self.lbl_time.configure(text=f"{current_str} / {total_str}")
            else:
                if self.lbl_time:
                    self.lbl_time.configure(text=lang_dict["time_default"])
        except Exception:
            pass

        self.after(200, self._update_playback_loop)

    def show_info(self):
        lang_dict = I18N[LANG]
        text = lang_dict["info_body"].format(
            app_name=APP_NAME,
            app_version=APP_VERSION,
            company=APP_COMPANY,
        )

        info_win = ctk.CTkToplevel(self)
        info_win.title(lang_dict["info_title"])
        info_win.geometry("540x440")
        info_win.resizable(False, False)
        info_win.grab_set()
        info_win.focus_force()
        info_win.lift()
        info_win.attributes("-topmost", True)
        info_win.after(200, lambda: info_win.attributes("-topmost", False))      

        content = ctk.CTkFrame(info_win, corner_radius=12)
        content.pack(fill="both", expand=True, padx=20, pady=20)

        lbl = ctk.CTkLabel(
            content,
            text=text,
            justify="left",
            anchor="nw",
            wraplength=500,
        )
        lbl.pack(fill="both", expand=True)

        bottom = ctk.CTkFrame(content)
        bottom.pack(fill="x", pady=(10, 0))
        bottom.columnconfigure(0, weight=1)

        def add_button(row: int, text: str, url: str):
            ctk.CTkButton(
                bottom,
                text=text,
                fg_color="transparent",
                text_color="dodgerblue",
                hover_color="gray25",
                width=140,
                command=lambda: webbrowser.open(url),
            ).grid(row=row, column=1, sticky="e", pady=3)

        add_button(0, lang_dict["link_website"], APP_WEBSITE)
        add_button(1, lang_dict["link_support"], f"mailto:{APP_SUPPORT_EMAIL}")
        add_button(2, lang_dict["link_github"], APP_GITHUB)

        ctk.CTkButton(
            bottom,
            text=lang_dict["ok_button"],
            width=90,
            command=info_win.destroy,
        ).grid(row=3, column=1, sticky="e", pady=(10, 0))

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    app = MediaPlayerApp()
    app.mainloop()

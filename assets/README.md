Demo assets placeholder

Place screenshots or a short GIF demonstrating the Streamlit UI in this folder.

Suggested filenames:
- `assets/demo.png` — a static screenshot
- `assets/demo.gif` — short screen recording showing interaction

Tip: create a short GIF with tools like `peek` (Linux), `LICEcap` (Windows/macOS), or by recording and converting with `ffmpeg`.

Example `ffmpeg` command to convert an MP4 to GIF (adjust `-ss` and `-t`):

```bash
ffmpeg -i demo.mp4 -ss 0 -t 6 -vf "fps=15,scale=800:-1:flags=lanczos" -gifflags -transdiff -y assets/demo.gif
```

Add the generated file here and update `README.md` to include `![Demo](assets/demo.gif)`.

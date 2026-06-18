import os
import sys
import shutil
from typing import Optional

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.progress import (
    Progress,
    SpinnerColumn,
    TextColumn,
    BarColumn,
    TaskProgressColumn,
    TimeRemainingColumn,
    DownloadColumn,
)
from rich.align import Align
from rich.text import Text
from rich import box
import yt_dlp

console = Console()

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def checkffmpeg():
    if not shutil.which('ffmpeg'):
        guide = """
[bold red]FFmpeg is not installed or not in your system PATH![/bold red]
[yellow]FFmpeg is required to extract and convert audio to MP3 or WAV formats efficiently.[/yellow]

[bold cyan]⚡ Quickest Windows Install (Windows 10/11):[/bold cyan]
1. Open PowerShell or Command Prompt.
2. Run this command: [bold green]winget install ffmpeg[/bold green]
3. Restart Zyre Downloader after installation finishes.

[bold cyan]🛠️ Manual Install (If winget doesn't work):[/bold cyan]
1. Go to [blue underline]https://www.gyan.dev/ffmpeg/builds/[/blue underline]
2. Download 'ffmpeg-release-essentials.zip' and extract it (e.g., to C:\\ffmpeg)
3. Press the [bold white]Windows Key[/bold white], type [bold white]"Environment Variables"[/bold white], and press Enter.
4. Click the [bold white]"Environment Variables"[/bold white] button at the bottom.
5. Under "System variables", find [bold white]"Path"[/bold white], select it, and click [bold white]"Edit"[/bold white].
6. Click [bold white]"New"[/bold white] and paste the path to the 'bin' folder you extracted (e.g., [green]C:\\ffmpeg\\bin[/green]).
7. Click OK on all windows and restart Zyre Downloader.
"""
        console.print(Panel(guide, title="[bold magenta]⚠️ FFmpeg Missing[/bold magenta]", border_style="red", box=box.ROUNDED))
        console.print()

def showbanner():
    cls()
    bannertext = """
    ███████╗██╗   ██╗██████╗ ███████╗
    ╚══███╔╝╚██╗ ██╔╝██╔══██╗██╔════╝
      ███╔╝  ╚████╔╝ ██████╔╝█████╗  
     ███╔╝    ╚██╔╝  ██╔══██╗██╔══╝  
    ███████╗   ██║   ██║  ██║███████╗
    ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝
    """
    bannerpanel = Panel(
        Align.center(
            Text(bannertext, style="bold cyan") + 
            Text("\n⚡ THE FASTEST YOUTUBE DOWNLOADER ⚡", style="bold yellow")
        ),
        box=box.DOUBLE,
        border_style="cyan",
        title="[bold magenta]Welcome to Zyre Downloader[/bold magenta]",
        subtitle="[bold dim]Fast • Efficient • Cool[/bold dim]"
    )
    console.print(bannerpanel)
    console.print()

class ytdlbar:
    def __init__(self):
        self.progress = Progress(
            SpinnerColumn(spinner_name="dots", style="cyan"),
            TextColumn("[bold blue]{task.description}"),
            BarColumn(bar_width=None, complete_style="cyan", finished_style="bold green"),
            TaskProgressColumn(),
            "•",
            DownloadColumn(),
            "•",
            TimeRemainingColumn(),
            console=console,
            expand=True
        )
        self.taskid = None
        self.started = False

    def updatebar(self, d):
        if d['status'] == 'downloading':
            if not self.started:
                self.progress.start()
                self.started = True
                
            if self.taskid is None:
                filename = d.get('filename', 'video')
                shortname = os.path.basename(filename)
                if len(shortname) > 40:
                    shortname = shortname[:37] + "..."
                self.taskid = self.progress.add_task(f"Downloading {shortname}", total=d.get('total_bytes') or d.get('total_bytes_estimate', 0))
            
            downloaded = d.get('downloaded_bytes', 0)
            total = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
            
            if total > 0:
                self.progress.update(self.taskid, completed=downloaded, total=total)

        elif d['status'] == 'finished':
            if self.taskid is not None:
                self.progress.update(self.taskid, completed=d.get('total_bytes', 100), total=d.get('total_bytes', 100))
            if self.started:
                self.progress.stop()
                self.started = False
            console.print(f"\n[bold green]✔ Download Complete![/bold green] Processing file...")

def getoptions(choice: str) -> dict:
    options = {
        'concurrent_fragment_downloads': 5,
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
    }

    if choice == '1':
        options.update({
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'merge_output_format': 'mp4',
        })
    elif choice == '2':
        options.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    elif choice == '3':
        options.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
            }],
        })
    elif choice == '4':
        options.update({
            'format': 'bestvideo+bestaudio/best',
        })
    elif choice == '5':
        formatstr = Prompt.ask("[bold cyan]?[/bold cyan] [bold white]Enter custom format (e.g., mkv, webm, flv)[/bold white]")
        options.update({
            'format': f'bestvideo[ext={formatstr}]+bestaudio/best[ext={formatstr}]/best',
            'merge_output_format': formatstr,
        })
    return options

def runapp():
    showbanner()
    checkffmpeg()
    
    url = Prompt.ask("[bold cyan]?[/bold cyan] [bold white]Enter the YouTube URL[/bold white]")
    if not url.strip():
        console.print("[bold red]❌ Invalid URL.[/bold red]")
        return

    console.print("\n[bold magenta]Select Output Format:[/bold magenta]")
    console.print("  [bold cyan]1.[/bold cyan] 🎬 MP4 (Video)")
    console.print("  [bold cyan]2.[/bold cyan] 🎵 MP3 (Audio)")
    console.print("  [bold cyan]3.[/bold cyan] 🎹 WAV (Audio Lossless)")
    console.print("  [bold cyan]4.[/bold cyan] 🌟 Best Available (Video + Audio, any extension)")
    console.print("  [bold cyan]5.[/bold cyan] 🔧 Other Format (Custom)")
    
    choice = Prompt.ask(
        "\n[bold cyan]?[/bold cyan] [bold white]Your choice[/bold white]",
        choices=["1", "2", "3", "4", "5"],
        default="1"
    )

    ydlopts = getoptions(choice)
    ydlopts['outtmpl'] = '%(title)s.%(ext)s'
    
    progressbar = ytdlbar()
    ydlopts['progress_hooks'] = [progressbar.updatebar]

    console.print("\n[bold yellow]⚡ Downloading...[/bold yellow]")
    
    try:
        with yt_dlp.YoutubeDL(ydlopts) as ydl:
            info = ydl.extract_info(url, download=False)
            title = info.get('title', 'Unknown Title')
            console.print(f"\n[bold green]Video Title:[/bold green] [white]{title}[/white]\n")
            
            ydl.download([url])
            
        console.print(Panel("[bold green]✨ Successfully downloaded by Zyre Downloader! ✨[/bold green]", box=box.ROUNDED, border_style="green"))

    except Exception as e:
        if progressbar.started:
            progressbar.progress.stop()
        console.print(f"\n[bold red]❌ An error occurred:[/bold red] {str(e)}")
        console.print("[yellow]💡 Note: Make sure you have FFmpeg installed on your system if you are extracting audio or merging formats.[/yellow]")

    if Confirm.ask("\n[bold cyan]?[/bold cyan] [bold white]Download another one?[/bold white]"):
        runapp()
    else:
        console.print("\n[bold magenta]Thank you for using Zyre Downloader. Stay cool! 😎[/bold magenta]\n")

if __name__ == "__main__":
    try:
        runapp()
    except KeyboardInterrupt:
        console.print("\n\n[bold red]❌ Download cancelled by user. Goodbye![/bold red]")
        sys.exit(0)

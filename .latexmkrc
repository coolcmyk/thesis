# Konfigurasi latexmk untuk templat skripsi.
#
# Kompilasi memakai -outdir=out, sehingga bibtex dijalankan dari dalam folder
# out dan tidak menemukan pustaka.bib. Baris berikut menambahkan folder proyek
# ke jalur pencarian BibTeX agar daftar pustaka tetap terbentuk.
use Cwd;
my $proyek = getcwd();
# Git Bash/MSYS melaporkan direktori sebagai /c/... sedangkan MiKTeX
# membutuhkan bentuk c:/...
$proyek =~ s{^/([A-Za-z])/}{$1:/};
ensure_path( 'BIBINPUTS', $proyek );

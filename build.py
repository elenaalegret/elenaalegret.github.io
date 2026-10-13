from pybtex.database.input import bibtex

def get_personal_data():
    name = ["Elena", "Alegret"]
    email = "elenaalegret@gmail.com"
    twitter = "elenaalegret"
    github = "elenaalegret"
    linkedin = "elena-alegret"
    bio_text = f"""
                <p>
                I am a Master’s student at <a href="https://ethz.ch/en.html" target="_blank">ETH Zurich</a>, majoring in Machine Learning, and a student researcher at the <a href="https://cvg.ethz.ch/" target="_blank">Computer Vision and Geometry (CVG) Lab</a>, where I work on <strong>generative models for 3D reconstruction</strong>, supervised by <a href="https://federicotombari.github.io/" target="_blank">Prof. Federico Tombari</a>, <a href="https://people.inf.ethz.ch/marc.pollefeys/" target="_blank">Prof. Marc Pollefeys</a>, <a href="https://cvg.ethz.ch/team/Dr-Daniel-Bela-Barath" target="_blank">Dániel Béla Baráth</a>, <a href="https://m-niemeyer.github.io/" target="_blank">Michael Niemeyer</a>, and <a href="https://li-kunyi.github.io/" target="_blank">Kunyi Li</a>.
                </p>
                <p>
                Before that, I was a research intern at TUM’s <a href="https://www.cs.cit.tum.de/camp/start/" target="_blank">CAMP Lab</a> (2025, Prof. Federico Tombari), where I carried out my Bachelor’s thesis for my B.Sc. in <strong>Artificial Intelligence</strong> at <a href="https://www.upc.edu/en" target="_blank">UPC</a>, during a one-year exchange; the work was published at <strong>3DV 2026</strong>.
                Earlier, I was a research intern at EPFL’s <a href="https://www.epfl.ch/labs/lts4/" target="_blank">LTS4 Lab</a> (2024, <a href="https://people.epfl.ch/pascal.frossard?lang=en" target="_blank">Prof. Pascal Frossard</a>), working on vision foundation models for medical imaging, and at the <a href="https://www.bsc.es/" target="_blank">Barcelona Supercomputing Center (BSC)</a> (2023–24).
                </p>
                <p>
                My research interests include generative models, 3D computer vision, 3D reconstruction, and scene understanding.
                </p>

                <p>Feel free to reach out by email!</p>
                <p class="links" style="text-align: center;">
                    <a href="https://elenaalegret.github.io/assets/pdf/CV_Elena_Alegret.pdf" target="_blank"><i class="fa fa-address-card fa-lg"></i> CV</a>
                    <a href="mailto:elenaalegret@gmail.com"><i class="far fa-envelope-open fa-lg"></i> Mail</a>
                    <a href="https://twitter.com/elenaalegret" target="_blank"><i class="fab fa-twitter fa-lg"></i> Twitter</a>
                    <a href="https://scholar.google.com/citations?user=RQzP41AAAAAJ&hl=en" target="_blank"><i class="fa-solid fa-book"></i> Scholar</a>
                    <a href="https://github.com/elenaalegret" target="_blank"><i class="fab fa-github fa-lg"></i> Github</a>
                    <a href="https://www.linkedin.com/in/elena-alegret" target="_blank"><i class="fab fa-linkedin fa-lg"></i> LinkedIn</a>
                    <button class="btn btn-link" type="button" data-toggle="collapse" data-target="#demo" data-toggle="collapse" ><i class="fa-solid fa-trophy"></i> Awards</button>
                    <div id="demo" class="collapse" style="text-align: left;">
                    <span style="font-weight: bold;">Awards:</span>
                    In 2025, I graduated with <strong>Highest Honors</strong> for my Bachelor’s thesis at <a href="https://www.tum.de/en/" target="_blank">TU Munich (TUM)</a>, supervised by Prof. Federico Tombari; the work was published at <strong>3DV 2026</strong> as a co-first-author paper.
                    In 2021, I received the <strong>Academic Excellence Award</strong> from the Government of Catalonia for ranking in the top 3% of the university entrance exams.
                </div>
                </p>
    """
    footer = """
            <div class="col-sm-12" style="">
                <p class="footer-note">
                    Template adapted from:
                    <a href="https://github.com/m-niemeyer/m-niemeyer.github.io" target="_blank">&#9883;</a> 
                    <a href="https://kashyap7x.github.io/" target="_blank">&#9883;</a>
                    <a href="https://kait0.github.io/" target="_blank">&#9883;</a>
                </p>
            </div>
    """
    return name, bio_text, footer

def get_author_dict():
    return {
        'Federico Tombari': 'https://www.cs.cit.tum.de/camp/members/senior-research-scientists/federico-tombari/',
        'Kunyi Li': 'https://li-kunyi.github.io/',
        'Nassir Navab': 'https://www.professoren.tum.de/en/navab-nassir',
        'Siyun Liang': 'https://siyun-liang.github.io/',
        'Sen Wang': 'https://scholar.google.com/citations?user=OxZ9S6oAAAAJ&hl=en',
        'Stefano Gasperini': 'https://www.cs.cit.tum.de/camp/members/stefano-gasperini/',
        'Michael Niemeyer': 'https://m-niemeyer.github.io/',
        }

def generate_person_html(persons, connection=", ", make_bold=True, make_bold_name='Elena Alegret', add_links=True):
    links = get_author_dict() if add_links else {}
    s = ""
    for p in persons:
        string_part_i = ""
        for name_part_i in p.get_part('first') + p.get_part('last'): 
            if string_part_i != "":
                string_part_i += " "
            string_part_i += name_part_i
        if string_part_i in links.keys():
            string_part_i = f'<a href="{links[string_part_i]}" target="_blank">{string_part_i}</a>'
        if make_bold and string_part_i == make_bold_name:
            string_part_i = f'<span style="font-weight: bold";>{make_bold_name}</span>'
        if p != persons[-1]:
            string_part_i += connection
        s += string_part_i
    return s

def get_paper_entry(entry_key, entry):
    s = """<div class="pub"> <div class="row"><div class="col-sm-3">"""
    s += f"""<img src="{entry.fields['img']}" class="img-fluid img-thumbnail" alt="Project image">"""
    s += """</div><div class="col-sm-9">"""

    if 'award' in entry.fields.keys():
        s += f"""<a class="pub-title" href="{entry.fields['html']}" target="_blank">{entry.fields['title']}</a> <span style="color: red;">({entry.fields['award']})</span><br>"""
    else:
        s += f"""<a class="pub-title" href="{entry.fields['html']}" target="_blank">{entry.fields['title']}</a> <br>"""

    s += f"""<span class="authors">{generate_person_html(entry.persons['author'])}</span> <br>"""
    s += f"""<span class="venue"><span style="font-style: italic;">{entry.fields['booktitle']}</span>, {entry.fields['year']}</span> <br>"""

    artefacts = {'html': 'Project Page', 'pdf': 'Paper', 'supp': 'Supplemental', 'video': 'Video', 'poster': 'Poster', 'code': 'Code'}
    i = 0
    for (k, v) in artefacts.items():
        if k in entry.fields.keys():
            if i > 0:
                s += ' / '
            s += f"""<a href="{entry.fields[k]}" target="_blank">{v}</a>"""
            i += 1
        else:
            print(f'[{entry_key}] Warning: Field {k} missing!')

    cite = "<pre><code>@InProceedings{" + f"{entry_key}, \n"
    cite += "\tauthor = {" + f"{generate_person_html(entry.persons['author'], make_bold=False, add_links=False, connection=' and ')}" + "}, \n"
    for entr in ['title', 'booktitle', 'year']:
        cite += f"\t{entr} = " + "{" + f"{entry.fields[entr]}" + "}, \n"
    cite += """}</pre></code>"""
    s += " / " + f"""<button class="btn btn-link" type="button" data-toggle="collapse" data-target="#collapse{entry_key}" aria-expanded="false" aria-controls="collapseExample">Expand bibtex</button><div class="collapse" id="collapse{entry_key}"><div class="card card-body">{cite}</div></div>"""
    s += """ </div> </div> </div>"""
    return s

def get_talk_entry(entry_key, entry):
    s = """<div class="pub"> <div class="row"><div class="col-sm-3">"""
    s += f"""<img src="{entry.fields['img']}" class="img-fluid img-thumbnail" alt="Project image">"""
    s += """</div><div class="col-sm-9">"""
    s += f"""{entry.fields['title']}<br>"""
    s += f"""<span style="font-style: italic;">{entry.fields['booktitle']}</span>, {entry.fields['year']} <br>"""

    artefacts = {'slides': 'Slides', 'video': 'Recording'}
    i = 0
    for (k, v) in artefacts.items():
        if k in entry.fields.keys():
            if i > 0:
                s += ' / '
            s += f"""<a href="{entry.fields[k]}" target="_blank">{v}</a>"""
            i += 1
        else:
            print(f'[{entry_key}] Warning: Field {k} missing!')
    s += """ </div> </div> </div>"""
    return s

def get_publications_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file('publication_list.bib')
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s+= get_paper_entry(k, bib_data.entries[k])
    return s

def get_talks_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file('talk_list.bib')
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s+= get_talk_entry(k, bib_data.entries[k])
    return s

def get_index_html():
    pub = get_publications_html()
    talks = get_talks_html()
    name, bio_text, footer = get_personal_data()
    s = f"""
    <!doctype html>
<html lang="en">

<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css" integrity="sha512-xh6O/CkQoPOWDdYTDqeRdPCVd1SpvCA9XXcUnZS2FmJNp1coAFzvtCN9BmamE+4aHK8yyUHUSCcJHgXloTyT2A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
  <style>
    body {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif; color: #333; font-size: 15.5px; line-height: 1.7; }}
    .container {{ max-width: 1000px; }}
    .display-4 {{ font-weight: 300; letter-spacing: -0.02em; }}

    /* Links: light blue with a soft gray underline */
    a, .btn-link {{ color: #4a8fc7; text-decoration: none; border-bottom: 1px solid #ddd; transition: color 0.15s, border-color 0.15s; }}
    a:hover, .btn-link:hover {{ color: #1f5f8b; text-decoration: none; border-bottom-color: #999; }}
    .btn-link {{ padding: 0; font-size: inherit; line-height: inherit; vertical-align: baseline; border-radius: 0; border-top: 0; border-left: 0; border-right: 0; }}
    .btn-link:focus {{ box-shadow: none; text-decoration: none; }}

    .bio p {{ text-align: justify; }}
    .links {{ margin-top: 1.5rem; font-size: 0.9rem; }}
    .links a, .links .btn-link {{ border-bottom: none; margin: 0 0.3rem; white-space: nowrap; }}
    .links i {{ margin-right: 0.25rem; }}

    h4 {{ font-size: 1.3rem; font-weight: 600; padding-bottom: 0.5rem; margin-bottom: 1.5rem; border-bottom: 1px solid #eee; }}
    .profile-img {{ width: 100%; max-width: 220px; border-radius: 12px; box-shadow: 0 4px 14px rgba(0, 0, 0, 0.08); }}

    .pub {{ margin-bottom: 2.2em; }}
    .pub-title {{ color: #222; font-weight: 600; border-bottom: none; }}
    .pub .authors a {{ color: #666; border-bottom: none; }}
    .pub .authors a:hover {{ color: #1f5f8b; }}
    .pub .venue {{ color: #777; }}
    .img-thumbnail {{ border-radius: 8px; border-color: #eee; padding: 0; }}

    .footer-note, .footer-note a {{ color: #aaa; font-size: 0.8rem; border-bottom: none; }}
  </style>

  <title>{name[0] + ' ' + name[1]}</title>
  <link rel="icon" type="image/x-icon" href="assets/favicon.ico">
</head>

<body>
    <div class="container">
        <div class="row">
            <div class="col-md-1"></div>
            <div class="col-md-10">
                <div class="row" style="margin-top: 3em;">
                    <div class="col-sm-12" style="margin-bottom: 1em;">
                    <h3 class="display-4" style="text-align: center;"><span style="font-weight: bold;">{name[0]}</span> {name[1]}</h3>
                    </div>
                    <br>
                    <div class="col-md-9 bio" style="">
                        {bio_text}
                    </div>
                    <div class="col-md-3" style="text-align: center;">
                        <img src="assets/img/profile.jpg" class="profile-img" alt="Profile picture">
                    </div>
                </div>
                <div class="row" style="margin-top: 1em;">
                    <div class="col-sm-12" style="">
                        <h4>Publications</h4>
                        {pub}
                    </div>
                </div>
                <!-- Talks: uncomment when talk_list.bib has entries
                <div class="row" style="margin-top: 3em;">
                    <div class="col-sm-12" style="">
                        <h4>Talks</h4>
                        {talks}
                    </div>
                </div>
                -->
                <div class="row" style="margin-top: 3em; margin-bottom: 1em;">
                    {footer}
                </div>
            </div>
            <div class="col-md-1"></div>
        </div>
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
      integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
      crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
      integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
      crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
      integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
      crossorigin="anonymous"></script>
</body>

</html>
    """
    return s


def write_index_html(filename='index.html'):
    s = get_index_html()
    with open(filename, 'w') as f:
        f.write(s)
    print(f'Written index content to {filename}.')

if __name__ == '__main__':
    write_index_html('index.html')

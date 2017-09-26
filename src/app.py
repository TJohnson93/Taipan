import sys
import json
from flask import Flask, render_template
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
POST_DIR = 'posts'

app = Flask(__name__)
flatpages = FlatPages(app)
freezer = Freezer(app)
app.config.from_object(__name__)

# Data Arrays
courses = [{ "course":"Diploma of Information Technology (Software Development)", "institute":"Gold Coast Institute of Tafe", "date_start":"2012", "date_end":"2012", "sprite":"path.jpg"}]

experiences = [{
        "organisation":"Queensland Health - eHealth",
        "organisation_sub":"Townsville QLD, Australia",
        "position": "Technology Officer",
        "date_start":"July 2017",
        "date_end":"Present (Fixed-Term Contract)",
        "description": "I have recently started working again at eHealth Queensland as a Technology Officer. Currently working in the Physical team, I support a multitude of devices, including; PC's, laptops and tablets, Windows 7 & 8.1, printers and label printers and any out-of-the-ordinary issues that may arrive. In the low periods I try and assist any other teams such as; virtual, comms and nets and Windows 10 to make efficient use of my time.",
        "task_lists": {},
        "attachments_available": False,
        "sprite":"",
        "hidden": False
    },{
        "organisation":"External IT",
        "organisation_sub":"Townsville QLD, Australia",
        "position": "Network and Systems Administrator",
        "date_start":"May 2017",
        "date_end":"July 2017",
        "description": "External IT is a small Managed Service Provider (MSP) based in Townsville supporting nearly 400 devices across 16 clients. Whilst employed I'll be managing most aspects of the clients Information Technology infrastructure including desktops, laptops, mobile devices, printers, Windows servers running Active Directory, VMware, Exchange, DHCP, DNS, Print Management and more, server backups, networking (switches, routers, firewalls, wireless access points). This is in addition to any project work that arises for any client.",
        "task_lists": {},
        "attachments_available": False,
        "sprite":"",
        "hidden": False
    },{
        "organisation":"Department of Justice & Attorney-General",
        "organisation_sub":"Townsville QLD, Australia",
        "position": "Level 2/3 Technical Support Officer",
        "date_start":"August 2016",
        "date_end":"April 2017 (Fixed-Term Contract)",
        "description": "I worked at the Department of Justice & Attorney General as a Level 2/3 Technical Support Officer for 9 months on a fixed-term contract, working with a major client (Queensland Corrective Services) and assist with support for over 3500 assets across Queensland.",
        "task_lists": {
            "Provide support for over 3500 assets",
            "Packaging, testing, and distributing software through SCCM",
            "Replacing 100s of workstations that are out of warranty",
            "Deploying applications to workstations using SCCM",
            "Create/Manage Accounts in Active Directory",
            "Creating scripts in Powershell to assist techs with support",
            "Assist in testing applications before deployment across the fleet",
            "Documenting easy to understand guides for general users",
            "Documenting articles for a newly created tech knowledgebase",
            "Escalating service calls and directing the support for issues to be resolved by third party companies",
            "Provide onsite repair work when applicable"
            },
        "attachments_available": False,
        "sprite":"",
        "hidden": False
    },{
        "organisation":"Queensland Health - eHealth",
        "organisation_sub":"Townsville QLD, Australia",
        "position": "Technology Officer",
        "date_start":"September 2015",
        "date_end":"June 2016 (Fixed-Term Contract)",
        "description": "I was brought onto the Windows 7 Project team at Queensland Health where I rolled out Windows 7 to over 4500 workstations across a multitude of sites including, Townsville, Kirwan, Ayr, Palm Island, Charters Towers, Richmond, Hughenden, and Ingham. My duties are as follows:",
        "task_lists": {
            "Workstation Replacements for workstations out of warranty",
            "Migrate workstations from Windows XP to Windows 7",
            "Create printer configuration profiles in Novell iPrint",
            "Assign Windows 7 drivers to printers in Novell iPrint",
            "Assign applications to workstations using SCCM",
            "Documenting work instruction how to's for other staff in the department"
            },
        "attachments_available": False,
        "sprite":"",
        "hidden": False
    },{
        "organisation":"Education Queensland",
        "organisation_sub":"Doomadgee QLD, Australia",
        "position": "Administration Officer (A/ Business Services Manager)",
        "date_start":"January 2015",
        "date_end":"May 2015",
        "description": "Whilst living in Doomadgee a remote indigenous town near the Gulf of Carpenteria I worked at Doomadgee State School as an Administration Officer. During this time I was acting Business Service Manager (BSM) for over approximately 1 1/2 months and performed the following:",
        "task_lists": {
            "Co-ordinated contract workers throughout the school",
            "Organised and managed casual staff members",
            "Organised rosters, pays and leave for casual & permanent staff",
            "Processing bills and invoices",
            "Processing purchase orders",
            "Handling phone, email and walk in enquires",
            "Enrolling students within the school",
            "Processed Blue-Card applications for staff"
            },
        "attachments_available": False,
        "sprite":"",
        "hidden": False
    },{
        "organisation":"Best Practice Australia",
        "organisation_sub":"Milton, Brisbane QLD, Australia",
        "position": "eSurvey Developer & Database Administrator",
        "date_start":"October 2013",
        "date_end":"December 2014",
        "description": "At Best Practice Australia I worked as an eSurvey Developer & Database Developer, during this time I performed the following duties and improved productivity by:",
        "task_lists": {
            "Creating eSurveys with IBM's SPSS Author",
            "Used advanced routing techniques in SPSS Author",
            "Utilised HTML, CSS, JavaScript and jQuery for eSurvey Templates",
            "Used cross-browser and speed enhancing techniques to ensure consistent performance",
            "Optimise tablet survey views by using the responsive web design approach",
            "Creating and utilising sprite sheets",
            "Using a DRY approach I modularised eSurvey components and was able to gain a 30% increase in development speed",
            "Consolidating eSurvey data using BPAs Microsoft Access databases",
            "Optimising Microsoft Databases for consistency and performance",
            "Creating documentation for the IT department",
            "Creating a training program for new eSurvey developer staff",
            "Training new IT staff members",
            "Improve productivity by developing small systems that utilised open source technologies (HTML5, CSS 3, SASS, JavaScript, jQuery, PHP and MySQL)",
            "Maintaining organisations workstations, switches, patch panels & servers"
            },
        "attachments_available": False,
        "sprite":"",
        "hidden": False
    }
]

general_skills = [{'Customer Service'},{'Loyal'},{'Independant'},{'Determined'},{'Quick Learner'},{'Communication'},{'Punctual'},{'Time Management'},{'Management'}]
technical_skills = [{'MS Office Suite'},{'MS Office 365'},{'MS Exchange'},{'MS SQL Server'},{'Apple iOS'},{'macOS'},{'Windows 7'},{'Windows 10'},{'Virtualisation'},{'Troubleshooting'}]
developer_skills = [{'HTML'},{ 'CSS'},{ 'Sass'},{ 'Less'},{ 'JavaScript'},{ 'jQuery'},{'Bootstrap'},{ 'Semantic-UI'},{ 'MySQL'},{ 'SQLite'},{ 'MS SQL'},{ 'Grunt'},{ 'Digital Ocean'}]

volunteer_work=[{
    'organisation': 'Beaudesert Warriors Rugby Union Club',
    'title': 'Rugby Coach',
    'date_start': 'Jan 2009',
    'date_end': 'Jan 2011',
    'description': 'In my mid teens I volunteered to coach Junior Rugby Union after a junior teams coach moved towns. I took on the responsibilities involved in teaching young players how to safely play rugby. I was able to teach them the ball skills and defensive skills required for them to progress in the later years. I made it a priority to train the players in a way that minimised injury and was still perform the many tasks required in a game of Rugby.',
    'attachments': [{'type': 'Written Reference', 'src': 'bwruc_ref'}]
}]

certificates = [
    {'title': 'CCNA Certification', 'company': 'Cisco', 'sprite': 'badge_ccna', 'completed': False, 'data': 'cisco_ccna'},
    {'title': 'Six Sigma Yellow Belt Certification', 'company': 'Yellow House', 'sprite': 'badge_sixsigma_yellow', 'completed': True, 'data': 'six_sigma_yellow'},
    {'title': 'Working with Children Blue Card','company': 'Queensland Government','sprite': 'badge_blue_card','completed': True,'data': 'lic_blue_card','expiry_date': '8/12/2017'},
    {'title': 'QLD Construction White Card', 'company': 'Blue Dog Training', 'sprite': 'badge_construction', 'completed': True, 'data': 'lic_white_card'},
    {'title': 'QLD RSA', 'company': 'Best Training', 'sprite': 'badge_rsa', 'completed': True, 'data': 'cert_rsa', 'expiry_date': '27/06/2016'}
]

@app.route("/")
def home():
    return render_template('home.html',
        courses=courses,
        experiences=experiences,
        general_skills=general_skills,
        technical_skills=technical_skills,
        developer_skills=developer_skills,
        volunteer_work=volunteer_work,
        # volunteer_work=importJson('src/volunteer_work.json'),
        certificates=certificates
    )

def importJson(file):
    json_data = importJson(file)
    return json_data

@app.route("/projects/")
def projects():
    return render_template('projects.html')


@app.route("/blog/")
def posts():
    posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
    # latest = sorted(posts, reverse=True,
        # key=lambda item:item['date'])
    posts.sort(key=lambda item:item['date'], reverse=True)
    return render_template('posts.html', posts=posts)
    # return render_template('posts.html', posts=latest[:2])

@app.route('/blog/<name>/')
def post(name):
    path = '{}/{}'.format(POST_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(host='127.0.0.1', debug=True)

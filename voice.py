# Ines's voice: warm, simple, excited, grateful, credits the team.
# Overrides the card blurbs and story paragraphs of PROJECTS and AWARDS by slug.
# Loaded by build.py (exec'd after the data lists are defined).

PROJECT_VOICE = {
 'tanit-xr': dict(
   card="The project I care about most. Volunteers in Tunisia and around the world scan our endangered heritage in 3D, one object at a time. 100+ free models so far!",
   paras=[
     "I started Tanit XR in 2025 to protect the Tunisian heritage I grew up with. We named it after Tanit, the Carthaginian goddess of protection, because that's exactly what we do.",
     "Volunteers in Tunisia scan statues, mosaics, stelae and carved stones with their phones, one object at a time. Volunteers around the world clean up the scans and turn them into free 3D models, AR lessons and our virtual museum. Everything we make is open and free, because heritage belongs to everyone.",
     "We started as an archive and became a community: 85+ volunteers on four continents meet every week to review scans, learn Tunisian history and help each other. So far we've published more than 100 models, and I was so happy when Niantic Spatial interviewed me about our scans at El Jem!",
     "We also teach. Our free Splats With Phones course shows anyone how to scan with the phone in their pocket. I honestly can't believe how far this little idea has come, and it's all thanks to our amazing volunteers."]),
 'shadows-of-tomorrow': dict(
   card="A climate installation where you see a damaged world alone, and a restored one the moment you hold someone's hand.",
   paras=[
     "Shadows of Tomorrow uses body tracking to place your silhouette inside climate data. When you stand alone, you see a world damaged by climate change. When you hold someone's hand, the scene heals.",
     "I wanted people to feel, in their own body, that we can only fix this together.",
     "It won the Excellence Award at the GFAA Biennial, presented by Miami's Chief Heat Officer Jane Gilbert and author Jeff Goodell, which meant so much to me. It ran for three months in the gallery and has been shown at Parsons in New York, MIT Reality Hack and Ringling College. It was also an MVP finalist in the AWE XR Prize Challenge."]),
 'smithsonian-futures': dict(
   card="I co-created the Future of Energy & Water experience for the Smithsonian's FUTURES exhibition in Washington, D.C. The show welcomed over 600,000 visitors!",
   paras=[
     "With my team at Froliq, I co-created the Future of Energy and Water experience for the Smithsonian's FUTURES exhibition in Washington, D.C. It was the Smithsonian's big 175th anniversary show, so this was a dream.",
     "Visitors got to explore how energy and water could work in a more sustainable future. More than 10,000 people tried our experience, and the whole exhibition welcomed over 600,000 visitors. I still get emotional thinking about it."]),
 'oracle-connected-hub': dict(
   card="The AR apps for Oracle's Connected Hub, a tiny working neighborhood with real solar panels and glowing power lines that comes to life in augmented reality.",
   paras=[
     "Oracle's Connected Hub is a scale model of a neighborhood that actually works. Real solar panels make electricity, power lines light up to show how energy moves, a wind turbine spins, and 16 little smart homes glow with what's happening inside. It's all connected to Oracle's real utility software.",
     "At Froliq, I build the AR apps that bring it to life. Point a tablet or headset at the model, or open the digital version from anywhere, and you can watch energy flow, see outages get predicted and fixed, and charge EVs in real time.",
     "The apps run on iPad, Windows, Meta Quest 3 and Apple Vision Pro, and they travel to events like DISTRIBUTECH, Oracle CloudWorld and the Energy Thought Summit. I love this project because it takes something people never get to see and makes it something they can play with."]),
 'nypa-vision-pro': dict(
   card="A Vision Pro app I built for the New York Power Authority, so you can walk around an energy grid floating in the room.",
   paras=[
     "For the New York Power Authority, I built an Apple Vision Pro app using Unity PolySpatial. It's a similar idea to the Oracle Connected Hub, but its own app, made for NYPA.",
     "The grid model floats in the room with you. You can walk around it, lean in and explore different grid scenarios with just your eyes and hands.",
     "It's still an early version, but walking around a grid floating in the room is so much more fun than looking at a diagram!"]),
 'vistra-tour': dict(
   card="A virtual safety tour of Vistra's Midlothian power plant, with four hazard zones you can explore in your browser or in VR.",
   paras=[
     "This is a guided virtual tour of Vistra's Midlothian power plant. It walks you through four hazard zones and teaches you what each danger is and how to stay safe around it. Everything is modeled and animated, so you really get to see the plant working.",
     "Vistra uses it for safety training, for meetings and at career fairs.",
     "We first built it for a VR platform, and then rebuilt it for the web with Unity and Needle Engine. Now anyone can open it in a browser, on a phone or in a VR headset, with nothing to install."]),
 'froliq-minigames': dict(
   card="VR games that teach kids about energy and the environment: sort trash in Recyclotopia, save energy in BungaLoad and power a town with wind in Fantastic Winds!",
   paras=[
     "These are VR mini-games we made at Froliq to teach energy and environmental education. In Recyclotopia you sort trash on a conveyor belt that keeps getting faster. In BungaLoad you walk through a house finding lights, appliances and leaky faucets that waste energy. In Fantastic Winds you fan wind turbines to light up a town!",
     "All three games connect through a fun lobby with three doors, a live leaderboard with gold, silver and bronze trophies, and a profile that tracks how much you've recycled, how much energy you've saved and how many houses you've powered. Play enough and you become an \"Efficiency Expert.\"",
     "Kids have played them at career fests, schools in Texas and workforce events. My favorite part is watching someone figure out that their small choices really add up."]),
 'sustainaball': dict(
   card="A soccer game where you kick a real ball at projected sustainability challenges. More than 100 students have played, and we brought it to the AWE 2026 playground!",
   paras=[
     "Sustainaball is a projection soccer game. You kick a real ball at a projected field, motion detection tracks it, and every kick answers a sustainability challenge. It gets the whole room moving and cheering.",
     "More than 100 students, from 7th graders to college students, have played it so far. We also brought it to the Augmented World Expo 2026 playground, and it was so fun to watch people from the XR industry line up to play!",
     "Kelly, my teammate at Froliq, and I had way too much fun building this one."]),
 'stevie': dict(
   card="An AR storytelling experience about energy that works anywhere, on the phones students already have.",
   paras=[
     "StEVie is an augmented reality story about energy. It's location based and runs on the phones and tablets students already carry, so they can play it anywhere.",
     "We tested it with the E4 youth community first. I love that it runs on the phones students already have, so nobody needs a headset."]),
 'exelon-stem': dict(
   card="VR simulations of real utility jobs for Exelon's five-year STEM program across all six of its utilities.",
   paras=[
     "Exelon runs a five-year STEM program across all six of its utilities, and at Froliq we build the VR part. Students put on a headset and try real jobs at a utility, at career fairs and in classrooms.",
     "The idea is to follow students from their first STEM day all the way to a job in energy. It makes me so happy to help a kid discover a job they never knew existed."]),
 'nuclear-capture': dict(
   card="We 3D-scanned the Davis-Besse nuclear power plant, from the turbine deck to the cooling tower, so staff can train in it on the web, in VR and in AR.",
   paras=[
     "A nuclear power plant isn't a place you can just walk around and practice in. So at Froliq, we used the PortalCam scanner to capture the Davis-Besse plant in 3D, including the turbine deck and the cooling tower.",
     "We turn the scans into Gaussian splats, the same technique I use for Tanit XR, so staff can explore a realistic version of the plant on the web, in VR or in AR before they ever step inside.",
     "It still amazes me that I use the same tools on a 2,000-year-old Roman stela and on a nuclear power plant!"]),
 'covid-reflections': dict(
   card="AR public art that traveled with mobile health clinics across Florida, California and Japan. More than 200 people got check-ups alongside it.",
   paras=[
     "Covid Reflections is an augmented reality public art installation that toured Florida, California and Japan, and it went hand in hand with real public health work.",
     "In Florida, it traveled with health check-up and vaccination trucks, and people got real check-ups while they were there. ABC, CBS and UF News all covered it, and we published the research behind it with ACM."]),
 'sparc': dict(
   card="An AR animation tool that lets anyone animate in 3D with their hands, no complicated menus or rigging needed.",
   paras=[
     "3D animation can be really hard to get into. Traditional software is full of menus, rigging and skinning that scare beginners away. spARc lets you animate right in augmented reality with both hands, without any of that.",
     "We designed it with feedback from focus groups. One of my favorite ideas is the round time slider. It replaces the usual long timeline, so your arms don't get tired and picking a keyframe in the air is much easier."]),
}

AWARD_VOICE = {
 'auggie-finalist': dict(
   card="Tanit XR was a finalist for Best Societal Impact at AWE 2026.",
   paras=[
     "I've been watching the Auggie Awards since I was a student, dreaming of being there one day. In January 2026, I put them on my vision board. In May, Tanit XR was announced as a finalist for Best Societal Impact!",
     "Thank you so much to everyone who voted for us. On the night of the ceremony at AWE in Long Beach, our team got one of the loudest cheers in the room, and I will never forget it.",
     "We didn't win this time, but the next day I saw a giant whale jump out of the ocean, and I'm taking that as a sign. We'll be back next year!"]),
 'ee-30-under-30': dict(
   card="I was named to the NAAEE EE 30 Under 30 Class of 2025, a list of young leaders changing environmental education around the world.",
   paras=[
     "Every year, the North American Association for Environmental Education picks 30 young leaders from around the world who are changing how people learn about the environment. I was so honored to be named to the Class of 2025!",
     "My path here started on a beach in Florida, when I realized that what I thought was sand was actually tiny pieces of plastic. Seeing it with my own eyes changed me more than any article ever did. That's why I make things you can see and touch.",
     "I've met so many kind people through it, teachers, scientists, artists. And this year, I got to help choose the next class as a judge!"]),
 'gfaa-excellence': dict(
   card="Shadows of Tomorrow won the Excellence Award at the GFAA Biennial, presented by Miami's Chief Heat Officer and author Jeff Goodell.",
   paras=[
     "My climate installation Shadows of Tomorrow won the Excellence Award at the Gainesville Fine Arts Association Biennial. The award was presented by Jane Gilbert, Miami's Chief Heat Officer, and Jeff Goodell, author of The Heat Will Kill You First. I admire both of them so much!",
     "It ran for three months as part of the HEAT exhibition. You can read all about the piece on the <a href=\"project-shadows-of-tomorrow.html\">Shadows of Tomorrow</a> page.",
     "Receiving it from people who work on extreme heat every day made it extra special."]),
 'ieee-best-paper': dict(
   card="A Best Paper Award at the 2023 IEEE Integrated STEM Education Conference, for research on teaching with mini VR game engines, with Dr. Angelos Barmpoutis and Wenbin Guo.",
   paras=[
     "At the University of Florida's Digital Worlds Institute, I worked with Professor Angelos Barmpoutis and Wenbin Guo on a question I really care about: how do you teach new technology so it actually sticks? Our answer was to have students build their own mini VR game engines instead of just using finished ones.",
     "Our paper, “Developing Mini VR Game Engines as an Engaging Learning Method for Digital Arts &amp; Sciences,” won a Best Paper Award at the 2023 IEEE Integrated STEM Education Conference.",
     "I still believe in learning by building. It's how we make games at Froliq and how we teach scanning at Tanit XR."]),
 'awe-xr-prize': dict(
   card="Shadows of Tomorrow made it to the MVP finalist stage of AWE's international XR Prize Challenge.",
   paras=[
     "The AWE XR Prize Challenge gets entries from all over the world, and Shadows of Tomorrow made it to the MVP finalist stage!",
     "Not bad for a piece that started in a small gallery in Gainesville! After this it traveled to MIT Reality Hack, Parsons and Ringling College."]),
 'hackathon-wins': dict(
   card="Hackathon wins supported by Google and IBM, and a tradition of printing our own award at MIT Reality Hack!",
   paras=[
     "During my master's at the University of Florida, my MiDAS cohort won a bunch of hackathons supported by organizations like Google and IBM. Some of those weekend projects actually worked!",
     "In 2026 MIT Reality Hack got cut short, so my team 3D-printed our own little award. <a href=\"blog-mit-reality-hack-2026.html\">Read the story</a>.",
     "Hackathons are where I test ideas fast. A few projects on this site started as a weekend prototype."]),
 'g4c-judge': dict(
   card="I've judged both the Games for Change Awards and their national Student Challenge.",
   paras=[
     "Games for Change celebrates games that tackle real-world problems, and I've been lucky to judge on both sides: the Games for Change Awards for the best impact games in the industry, and the Student Challenge, the biggest student game design competition in the U.S.",
     "Judging the students is my favorite. Seeing young people make games about climate, health and their own communities gives me so much hope.",
     "I really believe people learn best by making things, and games are a great way to talk about hard topics."]),
}

for _p in PROJECTS:
    _v = PROJECT_VOICE.get(_p['slug'])
    if _v:
        _p.update(_v)
for _a in AWARDS:
    _v = AWARD_VOICE.get(_a['slug'])
    if _v:
        _a.update(_v)

# Ines's voice: warm, simple, excited, grateful, credits the team.
# Overrides the card blurbs and story paragraphs of PROJECTS and AWARDS by slug.
# Loaded by build.py (exec'd after the data lists are defined).

PROJECT_VOICE = {
 'tanit-xr': dict(
   card="My heart project! Tunisia's first open-source heritage archive. Our volunteers have scanned 80+ artifacts across 20 sites, all free for anyone to explore.",
   paras=[
     "I started Tanit XR in 2025 to protect the Tunisian heritage I grew up with. We named it after Tanit, the Carthaginian goddess of protection, because that's exactly what we do.",
     "Volunteers on the ground scan statues, mosaics and archaeological sites with their phones, and our community around the world turns those scans into 3D models, a virtual museum and AR experiences. Everything we make is open and free, because heritage belongs to everyone.",
     "So far we've documented more than 80 artifacts across 20 sites. Our reconstruction of the El Jem Amphitheater is the largest one we've done, and I was so happy when Niantic Spatial shared it!",
     "We also teach. Our free Splats With Phones course shows anyone how to scan with the phone in their pocket. I honestly can't believe how far this little idea has come, and it's all thanks to our amazing volunteers."]),
 'shadows-of-tomorrow': dict(
   card="A climate installation where you see a damaged world alone, and a restored one the moment you hold someone's hand.",
   paras=[
     "Shadows of Tomorrow uses body tracking to place your silhouette inside climate data. When you stand alone, you see a world damaged by climate change. When you hold someone's hand, the scene heals.",
     "I wanted people to feel that we can only fix this together, not just read about it.",
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
     "It's still an early version, but it was such a fun way to imagine what learning about the grid could feel like when the screen disappears."]),
 'vistra-tour': dict(
   card="A virtual safety tour of Vistra's Midlothian power plant, with four hazard zones you can explore in your browser or in VR.",
   paras=[
     "This is a guided virtual tour of Vistra's Midlothian power plant. It walks you through four hazard zones and teaches you what each danger is and how to stay safe around it. Everything is modeled and animated, so you really get to see the plant working.",
     "Plant managers, directors and leaders at Vistra use it for safety training, for meetings with stakeholders and at career fairs.",
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
     "Kelly and I had way too much fun building this one."]),
 'stevie': dict(
   card="An AR storytelling experience about energy that works anywhere, on the phones students already have.",
   paras=[
     "StEVie is an augmented reality story about energy. It's location based and runs on the phones and tablets students already carry, so they can play it anywhere.",
     "About 30 young people from the E4 youth community have played it so far. I love that it meets students where they are, with the devices they already have."]),
 'exelon-stem': dict(
   card="VR simulations of real utility jobs for Exelon's five-year STEM program across all six of its utilities.",
   paras=[
     "Exelon runs a five-year STEM program across all six of its utilities, and at Froliq we build the VR part. Students get to step into real utility jobs, the ones that keep the lights on, at career fairs and in classrooms.",
     "The program works with teachers and community partners to help students go from their first taste of STEM to a real career in energy. It makes me so happy to help a kid discover a job they never knew existed."]),
 'nuclear-capture': dict(
   card="We 3D-scanned the Davis-Besse nuclear power plant, from the turbine deck to the cooling tower, so staff can train in it on the web, in VR and in AR.",
   paras=[
     "A nuclear power plant isn't a place you can just walk around and practice in. So at Froliq, we used the PortalCam scanner to capture the Davis-Besse plant in 3D, including the turbine deck and the cooling tower.",
     "We turn the scans into Gaussian splats, the same technique I use for Tanit XR, so staff can explore a realistic version of the plant on the web, in VR or in AR before they ever step inside.",
     "It still amazes me that I use the same tools to preserve an almost 2,000-year-old amphitheater and a nuclear power plant!"]),
 'covid-reflections': dict(
   card="AR public art that traveled with mobile health clinics across Florida, California and Japan. More than 200 people got check-ups alongside it.",
   paras=[
     "Covid Reflections is an augmented reality public art installation that toured Florida, California and Japan, and it went hand in hand with real public health work.",
     "In Florida, it traveled with health check-up and vaccination trucks, and more than 200 people got check-ups while they were there. ABC, CBS and UF News all covered it, and we published the research behind it with ACM."]),
 'sparc': dict(
   card="An AR animation tool that lets anyone animate in 3D with their hands, no complicated menus or rigging needed.",
   paras=[
     "3D animation can be really hard to get into. Traditional software is full of menus, rigging and skinning that scare beginners away. spARc lets you animate right in augmented reality with both hands, without any of that.",
     "We designed it with feedback from focus groups. One of my favorite ideas is the round time slider. It replaces the usual long timeline, so your arms don't get tired and picking a keyframe in the air is much easier."]),
}

AWARD_VOICE = {
 'auggie-finalist': dict(
   card="The Auggies are the XR industry's biggest awards, and Tanit XR was a finalist for Best Societal Impact! I had put them on my vision board in January.",
   paras=[
     "I've been watching the Auggie Awards since I was a student, dreaming of being there one day. In January 2026, I put them on my vision board. In May, Tanit XR was announced as a finalist for Best Societal Impact!",
     "Thank you so much to everyone who voted for us. On the night of the ceremony at AWE in Long Beach, our team got one of the loudest cheers in the room, and I will never forget it.",
     "We didn't win this time, but the next day I saw a giant whale jump out of the ocean, and I'm taking that as a sign. We'll be back next year!"]),
 'ee-30-under-30': dict(
   card="I was named to the NAAEE EE 30 Under 30 Class of 2025, a list of young leaders changing environmental education around the world.",
   paras=[
     "Every year, the North American Association for Environmental Education picks 30 young leaders from around the world who are changing how people learn about the environment. I was so honored to be named to the Class of 2025!",
     "My path here started on a beach in Florida, when I realized that what I thought was sand was actually tiny pieces of plastic. That moment taught me that seeing a problem with your own eyes changes you in a way facts on a page never can. It's the idea behind almost everything I make.",
     "Being part of this community of educators, scientists and artists has been such a gift. And this year, I got to help choose the next class as a judge!"]),
 'gfaa-excellence': dict(
   card="Shadows of Tomorrow won the Excellence Award at the GFAA Biennial, presented by Miami's Chief Heat Officer and author Jeff Goodell.",
   paras=[
     "My climate installation Shadows of Tomorrow won the Excellence Award at the Gainesville Fine Arts Association Biennial. The award was presented by Jane Gilbert, Miami's Chief Heat Officer, and Jeff Goodell, author of The Heat Will Kill You First. I admire both of them so much!",
     "In the piece, your silhouette appears inside climate data. Alone, you see a damaged world, and when you hold someone's hand, it heals. It ran for three months as part of the HEAT exhibition.",
     "Receiving it from people who work on extreme heat every day made it extra special."]),
 'ieee-best-paper': dict(
   card="A Best Paper Award at the 2023 IEEE Integrated STEM Education Conference, for research on teaching with mini VR game engines, with Dr. Angelos Barmpoutis and Wenbin Guo.",
   paras=[
     "At the University of Florida's Digital Worlds Institute, I worked with Professor Angelos Barmpoutis and Wenbin Guo on a question I really care about: how do you teach new technology so it actually sticks? Our answer was to have students build their own mini VR game engines instead of just using finished ones.",
     "Our paper, “Developing Mini VR Game Engines as an Engaging Learning Method for Digital Arts &amp; Sciences,” won a Best Paper Award at the 2023 IEEE Integrated STEM Education Conference.",
     "Learning by building is something I believe in so much, and it's still behind everything I do, from the games at Froliq to the scanning workshops at Tanit XR."]),
 'awe-xr-prize': dict(
   card="Shadows of Tomorrow made it to the MVP finalist stage of AWE's international XR Prize Challenge.",
   paras=[
     "The AWE XR Prize Challenge gets entries from all over the world, and Shadows of Tomorrow made it to the MVP finalist stage!",
     "It was such a big moment for a piece that started in a small local gallery, and it opened the doors that later took it to MIT Reality Hack, Parsons and Ringling College."]),
 'hackathon-wins': dict(
   card="Hackathon wins supported by Google and IBM, and a tradition of printing our own award at MIT Reality Hack!",
   paras=[
     "During my master's at the University of Florida, my MiDAS cohort won a bunch of hackathons supported by organizations like Google and IBM. We turned weekend sprints into real working prototypes.",
     "I keep going back to MIT Reality Hack for the community. In 2026 the event got cut short, so my team 3D-printed our own little award. It's honestly one of my favorite trophies!",
     "Hackathons are where I try the fastest version of an idea, and more than one project on this site started as a 48-hour prototype."]),
 'g4c-judge': dict(
   card="I've judged both the Games for Change Awards and their national Student Challenge.",
   paras=[
     "Games for Change celebrates games that tackle real-world problems, and I've been lucky to judge on both sides: the Games for Change Awards for the best impact games in the industry, and the Student Challenge, the biggest student game design competition in the U.S.",
     "Judging the students is my favorite. Seeing young people make games about climate, health and their own communities gives me so much hope.",
     "I really believe people learn best by making things, and that games can be a serious way to talk about serious topics."]),
}

for _p in PROJECTS:
    _v = PROJECT_VOICE.get(_p['slug'])
    if _v:
        _p.update(_v)
for _a in AWARDS:
    _v = AWARD_VOICE.get(_a['slug'])
    if _v:
        _a.update(_v)

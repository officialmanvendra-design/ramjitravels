import os
import re

NAV_INNER = """        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-20">
                <a href="index.html" class="flex items-center gap-3">
                    <img src="assets/images/logo.png" alt="Ramji Travels Logo" class="h-[104px] w-[104px] object-contain" onerror="this.src='https://placehold.co/100x100?text=Logo'">
                    <span class="text-2xl font-extrabold text-brand-blue dark:text-white tracking-tight">Ramji <span class="text-brand-orange">Travels</span></span>
                </a>
                <ul class="hidden md:flex space-x-6 items-center">
                    <li><a href="index.html" class="text-gray-800 dark:text-gray-100 hover:text-brand-orange font-medium transition-colors">Home</a></li>
                    <li><a href="destinations.html" class="text-gray-800 dark:text-gray-100 hover:text-brand-orange font-medium transition-colors">Destinations</a></li>
                    <li><a href="packages.html" class="text-gray-800 dark:text-gray-100 hover:text-brand-orange font-medium transition-colors">Packages</a></li>
                    <li><a href="gallery.html" class="text-gray-800 dark:text-gray-100 hover:text-brand-orange font-medium transition-colors">Gallery</a></li>
                    <li><a href="cab-booking.html" class="text-gray-800 dark:text-gray-100 hover:text-brand-orange font-medium transition-colors">Cab Booking</a></li>
                    <li><a href="itinerary-builder.html" class="text-gray-800 dark:text-gray-100 hover:text-brand-orange font-medium transition-colors">Plan Itinerary</a></li>
                    <li><a href="about.html" class="text-gray-800 dark:text-gray-100 hover:text-brand-orange font-medium transition-colors">About Us</a></li>
                </ul>
                <div class="hidden md:flex space-x-4 items-center">
                    <a href="contact.html" class="text-brand-blue dark:text-white font-medium hover:text-brand-orange dark:hover:text-brand-orange transition-colors self-center">Contact</a>
                    <button id="login-btn" onclick="document.getElementById('auth-modal').classList.remove('hidden')" class="text-gray-800 dark:text-gray-100 hover:text-brand-orange font-medium transition-colors">Login / Sign Up</button>
                    
                    <button class="theme-toggle-btn p-2 rounded-full hover:bg-gray-100 dark:bg-slate-800 dark:hover:bg-slate-700 transition-colors text-gray-600 dark:text-gray-300 ml-2" aria-label="Toggle Dark Mode">
                        <svg class="theme-icon-sun w-5 h-5 hidden" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
                        <svg class="theme-icon-moon w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path></svg>
                    </button>
                    <a id="profile-btn" href="profile.html" class="hidden text-gray-800 dark:text-gray-100 hover:text-brand-orange font-medium transition-colors flex items-center gap-2" title="My Profile">
                        <img src="https://ui-avatars.com/api/?name=User&background=0b2e59&color=fff" alt="Profile" class="w-8 h-8 rounded-full border-2 border-brand-blue dark:border-white">
                    </a>
                    <a href="booking.html" class="bg-brand-orange text-white px-6 py-2 rounded-full font-semibold hover:bg-orange-600 transition-all shadow-lg hover:shadow-xl transform hover:-translate-y-0.5">Book Now</a>
                </div>
            </div>
        </div>"""

files_to_update = [
    "destinations.html",
    "packages.html",
    "cab-booking.html",
    "itinerary-builder.html",
    "about.html",
    "contact.html",
    "package-details.html",
    "destination-detail.html",
    "gallery.html",
    "booking.html"
]

for filename in files_to_update:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Regex to find everything between <nav ...> and </nav>
        # Match <nav followed by anything except > then >, then match anything lazily, then </nav>
        pattern = re.compile(r'(<nav[^>]*>)(.*?)(</nav>)', re.DOTALL | re.IGNORECASE)
        
        new_content = pattern.sub(rf'\1\n{NAV_INNER}\n\3', content, count=1)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"Skipped {filename}")

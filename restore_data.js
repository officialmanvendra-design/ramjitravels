const url = 'https://qshdfoxntmqszvkqsrtv.supabase.co/rest/v1/travel_packages';
const headers = {
  apikey: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFzaGRmb3hudG1xc3p2a3FzcnR2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODIyODMwNTUsImV4cCI6MjA5Nzg1OTA1NX0.lsjI0qtTSIbxIvX_rcHV0ocm7rEXtnsiB1g5s00HkJI',
  Authorization: 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFzaGRmb3hudG1xc3p2a3FzcnR2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODIyODMwNTUsImV4cCI6MjA5Nzg1OTA1NX0.lsjI0qtTSIbxIvX_rcHV0ocm7rEXtnsiB1g5s00HkJI',
  'Content-Type': 'application/json',
  Prefer: 'return=representation'
};

const packageData = {
  id: '8ff65822-e4c3-496e-9fc4-2abe46cc90dc',
  title: 'Majestic Kerala Backwaters',
  description: 'Experience the serene beauty of Alleppey backwaters and lush tea gardens of Munnar.',
  price: 12500,
  duration_days: 5,
  includes: [ 'Daily Breakfast', 'Houseboat Stay', 'Airport Transfers' ],
  exclusions: [ 'Flights', 'Personal Expenses' ],
  image_url: 'https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?auto=format&fit=crop&w=800&q=80',
  hotel_details: '3-Star Premium Hotels',
  vehicle_details: 'Private AC Sedan',
  day_wise_itinerary: [
    { title: 'Day 1: Arrival', description: 'Arrive in Kerala and transfer to hotel.' },
    { title: 'Day 2: Houseboat', description: 'Stay overnight in a premium houseboat on the backwaters.' }
  ]
};

fetch(url, {
  method: 'POST',
  headers: headers,
  body: JSON.stringify(packageData)
})
.then(r => r.json())
.then(data => console.log('Successfully restored package:', data))
.catch(e => console.error('Error:', e));

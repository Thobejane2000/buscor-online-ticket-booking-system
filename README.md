#####################################################################################################################
HOW TO RUN APP
#####################################################################################################################
"# BuscorTickets" 
the codes for running the project

install visual studio  code 
install python external 
on CMD after installing python type pip install virtualenv

on vs code run the following terminals:

cd env/Scripts
cmd 
activate
cd ..
cd ..

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

#####################################################################################################################
#####################################################################################################################




Developed a fully functional and dynamic bus ticket booking website using **Python Django**, designed to streamline the process of managing and booking bus tickets online. The platform integrates secure payment processing through the **PayFast API**, enabling clients to make real-time payments with confidence. The system is built with a clear separation between the admin and client interfaces, each tailored to meet the specific needs of users.

### Admin Interface:  
The admin panel is a powerful management dashboard that provides comprehensive **CRUD (Create, Read, Update, Delete)** functionality for efficiently handling key aspects of the business, including:  
- **Bus Management:** Add, edit, and remove buses from the system, with options to define seating capacity, bus type, and operator details.  
- **Route Management:** Create and manage routes, specifying departure and arrival cities, intermediate stops, and travel distances.  
- **Schedule Management:** Configure bus schedules by setting departure times, estimated travel durations, and available seat counts for each trip.  
- **Booking Management:** View and manage customer bookings, update statuses, and monitor seat occupancy in real time. The admin can also generate reports on sales, occupancy rates, and cancellations to improve business operations.

### Client Interface:  
The client side offers a seamless and user-friendly experience, allowing users to:  
- **Search for Buses:** Enter their departure and destination locations, along with preferred travel dates, to view a list of available buses and routes.  
- **Real-Time Seat Availability:** Check the availability of seats for each trip, updated dynamically based on bookings and cancellations.  
- **Booking Tickets:** Select seats and complete the booking process through a secure and intuitive interface. Clients can review trip details, fare breakdowns, and payment options before finalizing their purchase.  
- **Secure Online Payments:** Make payments through the **PayFast API**, ensuring encrypted transactions and providing clients with various payment methods, including credit cards, debit cards, and mobile wallets.  

### Key Features:  
- **Mobile Responsiveness:** The website is fully optimized for both desktop and mobile devices, ensuring a consistent and intuitive experience across all screen sizes.  
- **Real-Time Updates:** The platform leverages Django’s capabilities to provide real-time updates on seat availability and booking status, reducing the chances of double-booking or overselling seats.  
- **Database Integration:** The system uses **SQLite** as its database backend, offering reliable and efficient data storage for bus details, routes, schedules, and bookings. Django’s ORM (Object-Relational Mapping) simplifies database interactions and ensures data integrity.  
- **User Authentication:** Both admins and clients have secure login systems, with user roles and permissions defined to prevent unauthorized access to sensitive data.  

This project emphasizes secure transactions, a seamless user experience, and efficient management of complex data, making it a robust solution for modern bus ticket booking needs.

-- 1) Find crime reports on Humphrey Street on July 28, 2024
SELECT * FROM crime_scene_reports WHERE month = 7 AND day = 28 AND street = 'Humphrey Street';

-- 2) Show interviews on July 28 mentioning the bakery (to get witness details)
SELECT * FROM interviews WHERE month = 7 AND day = 28 AND transcript LIKE '%bakery%';

-- 3) Check bakery security logs around the theft time (10:15 – witnesses said thief left then)
SELECT * FROM bakery_security_logs
WHERE year = 2024 AND month = 7 AND day = 28
AND hour = 10 AND minute BETWEEN 15 AND 25;

-- 4) Look up ATM activity at Leggett Street the same day (Eugene said he saw thief at ATM)
SELECT * FROM atm_transactions
WHERE year = 2024 AND month = 7 AND day = 28
AND atm_location = 'Leggett Street';

-- 5) Map suspicious account numbers to people and their license plates
SELECT people.name, people.license_plate, bank_accounts.account_number
FROM bank_accounts
JOIN people ON bank_accounts.person_id = people.id
WHERE bank_accounts.account_number IN (
  28500762, 28296815, 76054385, 49610011,
  16153065, 25506511, 81061156, 26013199
);

-- 6) Check short phone calls on July 28 (Raymond heard a short call from thief asking to buy a ticket)
SELECT caller, receiver, duration
FROM phone_calls
WHERE year = 2024 AND month = 7 AND day = 28
AND duration < 60;

-- 7) Look up phone owner for the number that was called (to find accomplice)
SELECT name FROM people WHERE phone_number = '(375) 555-8161';

-- 8) Find the earliest flight out the next day (July 29) and its destination
SELECT id, origin_airport_id, destination_airport_id, hour, minute
FROM flights
WHERE year = 2024 AND month = 7 AND day = 29
ORDER BY hour, minute
LIMIT 1;

-- 9) Who was on that flight?
SELECT people.name
FROM passengers
JOIN people ON passengers.passport_number = people.passport_number
WHERE passengers.flight_id = 36;

-- 10) What city is the destination airport?
SELECT city, full_name FROM airports WHERE id = 4;

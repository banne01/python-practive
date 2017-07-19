	
semaphore mutex = 1;                 // Controls access to the reader count
semaphore db = 1;                    // Controls access to the database
int reader_count;                    // The number of reading processes accessing the data

Reader()
{
  while (TRUE) {                     // loop forever
     down(&mutex);                          // gain access to reader_count
     reader_count = reader_count + 1;       // increment the reader_count
     if (reader_count == 1)
         down(&db);                         // if this is the first process to read the database,
                                            // a down on db is executed to prevent access to the 
                                            // database by a writing process
     up(&mutex);                            // allow other processes to access reader_count
     read_db();                             // read the database
     down(&mutex);                          // gain access to reader_count
     reader_count = reader_count - 1;       // decrement reader_count
     if (reader_count == 0)
         up(&db);                           // if there are no more processes reading from the 
                                            // database, allow writing process to access the data
     up(&mutex);                            // allow other processes to access reader_countuse_data();
                                            // use the data read from the database (non-critical)
}

Writer()
{
  while (TRUE) {                     // loop forever
     create_data();                         // create data to enter into database (non-critical)
     down(&db);                             // gain access to the database
     write_db();                            // write information to the database
     up(&db);                               // release exclusive access to the database
}


// number of readers
int readcount = 0;
// mutual exclusion to readcount
Semaphore mutex = 1;
// exclusive writer or reader
Semaphore w_or_r = 1;
writer {
	wait(w_or_r); // lock out readers
	Write;
	signal(w_or_r); // up for grabs
}
//Readers/Writers
reader {
	wait(mutex); // lock readcount
	readcount += 1; // one more reader
	if (readcount == 1)
		wait(w_or_r); // synch w/ writers
	signal(mutex); // unlock readcount
	Read;
	wait(mutex); // lock readcount
	readcount -= 1; // one less reader
	if (readcount == 0)
	signal(w_or_r); // up for grabs
	signal(mutex); // unlock readcount}

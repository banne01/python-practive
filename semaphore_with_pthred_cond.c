pthread_mutex_t count_lock;
pthread_cond_t count_nonzero;
unsigned int count;

init(c){
	count = c;
	// initiazize thread and mutex
}
sem_down()
{
    pthread_mutex_lock(&count_lock);
    while (count == 0)
        pthread_cond_wait(&count_nonzero, &count_lock);
    count = count - 1;
    pthread_mutex_unlock(&count_lock);
}

sem_up()
{
    pthread_mutex_lock(&count_lock);
    if (count == 0)
        pthread_cond_signal(&count_nonzero);
    count = count + 1;
    pthread_mutex_unlock(&count_lock);
}


#!/bin/bash


PIDFILE=WEBAPP.PID
ENVINI=development.ini

start_app() {
    #start server
    echo 'start app' 
    source ../bin/activate
    ../bin/gunicorn --paste development.ini -D --log-file=./run.log -p $PIDFILE

}

stop_app(){
    if [ -e $PIDFILE ]; then  
        echo 'stop app'
        pid=$(cat $PIDFILE)    
        if [ $pid > 0 ]; then 
            #stop server
            echo 'kill app pid' $pid
            #rm $PIDFILE
            #kill -9 $pid
            kill   $pid    
        fi    
    fi   
}

 





case "$1" in

        start)

                start_app

        ;;

        stop)

                stop_app

        ;;

        restart)

                stop_app

                sleep 2

                start_app

        ;;

        *)

                echo ' * Usage: appctl.sh  {start|stop|restart}'

                exit 1

        ;;

esac
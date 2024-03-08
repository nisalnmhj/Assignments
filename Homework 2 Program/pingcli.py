#Name: Nishan Maharjan
#Section: 03
#Date: 3/7/24
#Description: Client sends "PING" and waits for Server reply. If gets a reply, then calculates RTT. At last, Calculates Minrtt, Maxrtt, total 
#packet sent, total received and lost
import socket
import sys
import time

def create_client():
    svr_name = "ecs-coding1.csus.edu" #name of server
    svr_port = 8001 #server port
    total_sent = 0
    total_received = 0
    total_rtt = 0
    min_rtt = float('inf') #consider min_rtt infinity
    max_rtt = 0
    rtt_avg = 0

    cli_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    for i in range(10):
        j = i + 1 
        message = f"PING {j}"
        start_time = time.time()
        cli_socket.sendto(message.encode(),(svr_name, svr_port ) )
        response, svr_address  = cli_socket.recvfrom(2048)
        end_time = time.time()
        rtt = round(( (end_time - start_time) * 1000), 2)
        if response.decode() == "PONG": 
            print(f"{response.decode() } - RTT: {rtt}ms " )
            rtt_avg = rtt_avg + rtt
            total_received += 1
            total_rtt += rtt
            min_rtt = min(min_rtt, rtt)
            max_rtt = max(max_rtt, rtt)
        else:
            print(f"Request Timed out for PING {j}")
        total_sent += 1
    Lost = total_sent - total_received
    Inpercent = ( Lost/ total_sent) * 100
    average_rtt = round( ( rtt_avg / total_sent), 2) 
    print(f"Ping Statistics: ")
    print(f"Packets: sent= {total_sent}, Received = {total_received}, Lost = {Lost} ({Inpercent}%) ")

    print(f"RTT statistics:  " )
    print(f"Minimum RTT: {min_rtt}ms , Maximum RTT: {max_rtt}ms , Average RTT:{average_rtt}ms  ")
    cli_socket.close()


def main():
    if len(sys.argv) != 3:
        print("Usage: python pingcli.py <server_ip> <server_port>")
        sys.exit(1)
    svr_ip = sys.argv[1]
    svr_port = int(sys.argv[2])
    create_client( )

if __name__ == "__main__":
    main()


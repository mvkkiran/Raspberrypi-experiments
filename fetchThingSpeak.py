Import urllib2
import json
READ_API_KEY='CVNPT25IOSZ936WI'
CHANNEL_ID='578014'
def main():
    conn = urllib2.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                           % (CHANNEL_ID,READ_API_KEY))

    response = conn.read()
    print("http status code=%s" % (conn.getcode()))
    data=json.loads(response)
    print(data['field1'],data['created_at'])
    print(data['field2'],data['created_at'])
    conn.close()

if __name__ == '__main__':
    main()
import flex.messaging.io.amf.client.AMFConnection;
import flex.messaging.io.amf.client.exceptions.ClientStatusException;
import flex.messaging.messages.RemotingMessage;

public class PythonService
{
	public static void main(String[] args)
    {
		AMFConnection amfConnection = new AMFConnection();

		String url = "http://demo.pyamf.org/gateway/recordset";
		String service = "service";
    
		try {
			amfConnection.connect(url);
		} catch (ClientStatusException cse) {
			System.out.println(cse);
			return;
		}

		RemotingMessage message = new RemotingMessage();
		message.setMessageId(flex.messaging.util.UUIDUtils.createUUID());
		message.setOperation("getLanguages");
		// message.setBody(a);
		// message.setSource("IntrospectClass");
		message.setDestination(service);

		amfConnection.setObjectEncoding(3);
		amfConnection.setInstantiateTypes(false);

		Object returnValue;
		try {
			returnValue = amfConnection.call(null, message);
		} catch (Exception cse) {
			cse.printStackTrace();
			
		} finally {
			amfConnection.close();
		}
	}

}
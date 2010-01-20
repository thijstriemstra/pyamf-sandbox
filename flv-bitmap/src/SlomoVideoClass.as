package
{
	import flash.display.BitmapData;
	import flash.errors.EOFError;
	import flash.events.ProgressEvent;
	import flash.system.System;
	import flash.utils.ByteArray;
	import flash.utils.clearInterval;
	import flash.utils.setInterval;
	
	import mx.containers.VBox;
	import mx.controls.Button;
	import mx.controls.Image;
	import mx.controls.TextArea;
	import mx.controls.VideoDisplay;
	import mx.core.BitmapAsset;
	import mx.core.Container;
	import mx.rpc.events.FaultEvent;
	import mx.rpc.events.ResultEvent;
	import mx.rpc.remoting.mxml.RemoteObject;

	/**
	 * @author Thijs Triemstra
	 */	 
	public class SlomoVideoClass extends VBox
	{
		private var imageCache		: Array;
	    private var recordingId		: Number;
	    private var count			: int = 0;
		private var lastBmp			: BitmapData;
	    private var playSlomoId		: Number;
	    private var slomoImage		: BitmapAsset;
		private var imageContainer	: Container;
		
		public var img				: Image;
		public var slomo_btn		: Button;
		public var vPlayer			: VideoDisplay;
		public var remoteObj		: RemoteObject;
		public var status_txt		: TextArea;
		
		private var speed			: Number = 300; // ms
	    private var recordPrecision	: Number = 30; // fps
	    private var videoName		: String = "NORMAL_LAP";
	    private var videoPath		: String = "assets/video/" + videoName + "_flv.flv";
	    
	    [Bindable]
	    public var gatewayUrl		: String = "http://localhost:8000";
	    
		/**
		 * @constructor
		 */	    
		public function SlomoVideoClass()
		{
			super();
		}
		
		public function init():void
	    {
	    	trace('\nGTI Project Test App');
	    	trace('====================\n');
	    	trace('Gateway: ' + gatewayUrl);
	    	trace('Video: ' + videoPath);
	    	trace('Speed: ' + speed + ' ms');
	    	trace('Precision: ' + recordPrecision + ' fps');
	    	
	    	slomo_btn.visible = false;
	    	imageCache = [];
	    	vPlayer.source = videoPath;
	    	vPlayer.load();
	    }
	    
	    private function snap():BitmapData
	    {
			var myBitmapData:BitmapData = new BitmapData(vPlayer.width,
														 vPlayer.height,
														 false, 0x00CCCCCC);
			myBitmapData.draw(vPlayer);
			
			return myBitmapData;
		}
		
		private function doRecord():void
		{
			if (vPlayer.playing)
			{
				imageCache.push(snap());
			}
		}
		
	    private function playRec():void
	    {
			recordingId = setInterval(doRecord, recordPrecision);
		}
	    
		public function startRecording():void
		{
			if (slomo_btn.label == "Start Recording")
			{
				slomo_btn.label = "Stop Recording";
				status_txt.text = "Recording...";
				imageCache = new Array();
				count = 0;
				vPlayer.play();
				playRec();
				playSlomoId = setInterval(showFrame, speed);
			}
			else
			{
				stoppedRecording();
			}
		}
		
		private function stoppedRecording():void
		{
			var fileName:String = videoName.toLowerCase() + '.amf3';
			
			slomo_btn.label = "Start Recording";
			status_txt.text = "Recording completed!\nTotal frames: " + count;
			
			// stop recording
			clearInterval(playSlomoId);
			vPlayer.stop();
			img.source = null;
			
			// convert image cache to ByteArray
			var ba:ByteArray = new ByteArray();
			try
			{
				// write data to ByteArray
				ba.writeMultiByte(imageCache.toString(), 'utf-8');
				ba.compress();
				
                // Write compressed ByteArray to remote service
				status_txt.text += "\nSaving data to '" + fileName + "'...";
          		remoteObj.saveData( fileName, ba );
            }
            catch( e:EOFError )
			{
                status_txt.text += "\n" + e;
            }
		}
		
		private function showFrame():void
		{
			count++;
			
			if (count < imageCache.length)
			{
				slomoImage = new BitmapAsset(BitmapData(imageCache[count]));
				img.source = slomoImage;

				status_txt.text = "Recording frame: " + (count-1);
				BitmapData(imageCache[count-1]).dispose();
			}
			else
			{
				stoppedRecording();
			}
		}
		
		public function onProgress(evt:ProgressEvent):void
		{
			var perc:int = Math.round(evt.bytesLoaded / evt.bytesTotal) * 100;
			
			if (perc == 100)
			{
				slomo_btn.visible = true;
			}
		}
		
		public function onFault( event:FaultEvent ):void
		{
			// Notify the user of the problem
            status_txt.text += "\nRemoting error: \n    " + event.fault.faultDetail;
		}
		
		public function onResult( re:ResultEvent ): void
        {
            var result:String = re.result as String;
            if (result == 'success')
            {
            	status_txt.text += "\nSaved data!";
            }
            else
            {
            	status_txt.text += "\nError saving data";
            }
            trace( result );
        }
	    
	}
}
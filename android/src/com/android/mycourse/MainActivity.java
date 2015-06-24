package com.android.mycourse;

import android.app.Activity;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.Menu;
import android.webkit.DownloadListener;
import android.webkit.ValueCallback;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

public class MainActivity extends Activity {
	public static final int FILECHOOSER_RESULTCODE = 1;
	private WebView webview;
	private ValueCallback<Uri> mUploadMessage;
	
	private class MyWebViewDownLoadListener implements DownloadListener {
        @Override  
        public void onDownloadStart(String url, String userAgent, String contentDisposition, String mimetype,  
                                    long contentLength) {  
            Uri uri = Uri.parse(url);  
            Intent intent = new Intent(Intent.ACTION_VIEW, uri);  
            startActivity(intent);  
        }
    }
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		
		webview = (WebView)findViewById(R.id.webView1);
		WebSettings settings = webview.getSettings();
		settings.setJavaScriptEnabled(true);
		//webview.loadUrl("file:///android_asset/Home.html");
		webview.setDownloadListener(new MyWebViewDownLoadListener());
		webview.setWebChromeClient(new WebChromeClient(){
	    	// For Android 3.0+  
	        public void openFileChooser(ValueCallback<Uri> uploadMsg) {
	        	System.out.println("here");
	            mUploadMessage = uploadMsg;    
	            Intent i = new Intent(Intent.ACTION_GET_CONTENT);    
	            i.addCategory(Intent.CATEGORY_OPENABLE);    
	            i.setType("image/*");    
	            MainActivity.this.startActivityForResult(Intent.createChooser(i,"File Chooser"), FILECHOOSER_RESULTCODE);
	        }  
	  
	        // For Android 3.0+  
	        public void openFileChooser( ValueCallback uploadMsg, String acceptType ) {
	        	System.out.println("here");
	            mUploadMessage = uploadMsg;  
	            Intent i = new Intent(Intent.ACTION_GET_CONTENT);  
	            i.addCategory(Intent.CATEGORY_OPENABLE);  
	            i.setType("*/*");  
	            MainActivity.this.startActivityForResult(  
	            Intent.createChooser(i, "File Browser"),  
	            FILECHOOSER_RESULTCODE);  
	        }  
	  
	        //For Android 4.1  
	        public void openFileChooser(ValueCallback<Uri> uploadMsg, String acceptType, String capture) {
	        	System.out.println("here");
	            mUploadMessage = uploadMsg;    
                Intent i = new Intent(Intent.ACTION_GET_CONTENT);    
                i.addCategory(Intent.CATEGORY_OPENABLE);    
	            i.setType("image/*");    
	            MainActivity.this.startActivityForResult( Intent.createChooser( i, "File Chooser" ), MainActivity.FILECHOOSER_RESULTCODE );  
	        }
		});
		
		//覆盖WebView默认使用第三方或系统默认浏览器打开网页的行为，使网页用WebView打开
	    webview.setWebViewClient(new WebViewClient(){
	        @Override
	        public boolean shouldOverrideUrlLoading(WebView view, String url) {
	            //返回值是true的时候控制去WebView打开，为false调用系统浏览器或第三方浏览器
	        	view.loadUrl(url);
	            return true;
	        }
	    });
	    webview.loadUrl("http://sysupj.sinaapp.com");
	}

	@Override 
	protected void onActivityResult(int requestCode, int resultCode, 
	        Intent intent) { 
	    if (requestCode == FILECHOOSER_RESULTCODE) { 
	    	if (null == mUploadMessage) return;    
            Uri result = intent == null || resultCode != RESULT_OK ? null    
                    : intent.getData();    
            mUploadMessage.onReceiveValue(result);    
            mUploadMessage = null;
	    } 
	}
	
	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

}

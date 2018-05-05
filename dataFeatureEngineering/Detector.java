
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Detector {
	
	public Detector() {}
	public String[] setupSpams() throws FileNotFoundException, IOException
	{
		String [] spams = new String[456];
		String file = "/home/hristian/Documents/enron/SpamWords.txt"; 
		try (BufferedReader br = new BufferedReader(new FileReader(file))) {
		    String line;
		    int i = 0; 
		    while ((line = br.readLine()) != null) { 
		    	spams[i] = line; 
		    	i++; 
		    }
		}
		
		return spams; 
	}
	public boolean subjectHasSpam(String line, String[] spams){
		boolean foundPhishing = false; 
    	for(int k = 0; k < 456; k++)
    	{
   			if(line.contains(spams[k]))
    		{
    			foundPhishing = true; 
   			}
       	}
    	
    	return foundPhishing; 
    }
	
	public static void main(String[] args) throws FileNotFoundException, IOException{
		Detector detect = new Detector(); 
		String [] spams = detect.setupSpams();
		int [] emails = new int[3957742];
		
		String file = "/home/hristian/Documents/enron/Data_Cleaning/emails.txt";  
		try (BufferedReader br = new BufferedReader(new FileReader(file))) {
		    String line;
		    int i = 0; 
		    int phishers = 0; 
		    while ((line = br.readLine()) != null) {
		    	
		    	
		    	if(detect.subjectHasSpam(line, spams))//This will read every line, not just subject but I thought I'd just show you an example of how it works
		    	{
		    		emails[i] = 1; 
		    		phishers++; 
		    	}
		    	else
		    	{
		    		emails[i] = 0; 
		    	}
		        i++; 
		    }
		    System.out.println(i); 
		    System.out.println(emails[1]);
		    System.out.println("Phishers found: " + phishers);
		}
	}

}

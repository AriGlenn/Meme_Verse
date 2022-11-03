//
//  ViewController.swift
//  Meme_Verse
//
//  Created by Ari Glenn on 4/12/17.
//  Copyright © 2017 Ari Glenn. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    @IBOutlet weak var Name: UILabel!
    @IBOutlet weak var ImageView: UIImageView!
    let swipeRight = UISwipeGestureRecognizer()
    let swipeLeft = UISwipeGestureRecognizer()
    var memeIDnumber = 0
    
    override func viewDidLoad(){
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        displayMeme(idNumber: memeIDnumber)
        
        swipeRight.addTarget(self, action: #selector(ViewController.swipedRight) )
        swipeRight.direction = .right
        self.view!.addGestureRecognizer(swipeRight)
        
        swipeLeft.addTarget(self, action: #selector(ViewController.swipedLeft) )
        swipeLeft.direction = .left
        self.view!.addGestureRecognizer(swipeLeft)
    }
    
    
    
    func swipedRight(){
        print("Right")
        
        memeIDnumber -= 1
        if memeIDnumber < 0{
        memeIDnumber = 0
            
        }
        displayMeme(idNumber: memeIDnumber)
    }
    
    func swipedLeft(){
        print("Left")
        
        memeIDnumber += 1
        displayMeme(idNumber: memeIDnumber)
    
    }
    
    
    func displayMeme(idNumber: Int){
        let String_idNumber = String(idNumber)
        print(String_idNumber)

        let url = URL(string: "http://127.0.0.1:5000/getall")
        let task = URLSession.shared.dataTask(with: url!) { (data, response, error) in
            if error != nil{
                print ("ERROR")
            }else{
                if let content = data{
                    do{
                        let json = try JSONSerialization.jsonObject(with: content, options: JSONSerialization.ReadingOptions.mutableContainers) as AnyObject
                        if let id = json[String_idNumber] as? NSDictionary
                        {
                            if let name = id["Name"]{
                                print(name)
                                self.Name.text = "\(name)"
                            }
                            if let urls = id["MemeUrls"] as? [String]{
                                print(urls)
                                //CHANGE 0 FROM URLS[0] TO LOOP THROUGH
                                let urlLink = urls[0]
                                print(urlLink)
                                let URLpath = urlLink
                                let url = NSURL(string: URLpath)
                                let data = NSData(contentsOf: url! as URL)
                                let img = UIImage(data: data! as Data)
                                self.ImageView.image = img
                                print("Added image to the UIView")
                                
                            }
                            
                        }
                    }
                    catch
                    {
                    }
                }
            }
        }
        task.resume()
    }
    

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    
}


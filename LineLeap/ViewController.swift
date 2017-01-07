//
//  ViewController.swift
//  LineLeap
//
//  Created by Jason Brill on 12/11/16.
//  Copyright © 2016 LineLeap. All rights reserved.
//

import UIKit
import QuartzCore

class ViewController: UIViewController {
    @IBOutlet weak var EmailTextField: UITextField!
    @IBOutlet weak var PasswordTestField: UITextField!

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        EmailTextField.layer.borderColor = UIColor.c1().cgColor
        PasswordTestField.layer.borderColor = UIColor.c1().cgColor

        let email = NSAttributedString(string: "Email", attributes: [NSForegroundColorAttributeName:UIColor.c5()])
        EmailTextField.attributedPlaceholder = email
        
        let pass = NSAttributedString(string: "Password", attributes: [NSForegroundColorAttributeName:UIColor.c5()])
        PasswordTestField.attributedPlaceholder = pass
        
//        let spacerView = UIView(frame:CGRect(x:0, y:0, width:10, height:10))
//        EmailTextField.leftViewMode = UITextFieldViewMode.always
//        EmailTextField.leftView = spacerView
//        
//        PasswordTestField.leftViewMode = UITextFieldViewMode.always
//        PasswordTestField.leftView = spacerView
        
        navigationController?.navigationBar.barTintColor = UIColor.c2()
        
        let logo = UIImage(named: "LOGO")
        let imageView = UIImageView(image:logo)
        self.navigationItem.titleView = imageView
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    @IBAction func LoginTapped(_ sender: UIButton) {
        UserController.sharedInstance.login(email: EmailTextField.text!, password: PasswordTestField.text!, onCompletion: {message in
            if (message != nil){
                let meetings = MeetingViewController(nibName: "MeetingViewController", bundle: nil)
                self.navigationController?.pushViewController(meetings, animated: true)
            }
        })
    }
    
    @IBAction func RegisterTapped(_ sender: UIButton) {
        print("HERE FOR REGISTER")
    }
}


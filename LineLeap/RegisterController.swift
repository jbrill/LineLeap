//
//  RegisterController.swift
//  LineLeap
//
//  Created by Jason Brill on 1/9/17.
//  Copyright © 2017 LineLeap. All rights reserved.
//

import UIKit

class RegisterController: UIViewController {
    @IBOutlet weak var NameTextField: UITextField!
    @IBOutlet weak var EmailTextField: UITextField!
    @IBOutlet weak var PasswordTextField: UITextField!
    @IBOutlet weak var ConfirmPasswordTextField: UITextField!

    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
        self.hideKeyboardWhenTappedAround()
        
        NameTextField.layer.borderColor = UIColor.c1().cgColor
        EmailTextField.layer.borderColor = UIColor.c1().cgColor
        PasswordTextField.layer.borderColor = UIColor.c1().cgColor
        ConfirmPasswordTextField.layer.borderColor = UIColor.c1().cgColor
        
        let name = NSAttributedString(string: "Name", attributes: [NSForegroundColorAttributeName:UIColor.c5()])
        NameTextField.attributedPlaceholder = name
        
        let email = NSAttributedString(string: "Email", attributes: [NSForegroundColorAttributeName:UIColor.c5()])
        EmailTextField.attributedPlaceholder = email
        
        let pass = NSAttributedString(string: "Password", attributes: [NSForegroundColorAttributeName:UIColor.c5()])
        PasswordTextField.attributedPlaceholder = pass
        
        let cpass = NSAttributedString(string: "Confirm Password", attributes: [NSForegroundColorAttributeName:UIColor.c5()])
        ConfirmPasswordTextField.attributedPlaceholder = cpass
        
        NameTextField.layer.sublayerTransform = CATransform3DMakeTranslation(15, 0, 0)
        PasswordTextField.layer.sublayerTransform = CATransform3DMakeTranslation(15, 0, 0)
        EmailTextField.layer.sublayerTransform = CATransform3DMakeTranslation(15, 0, 0)
        ConfirmPasswordTextField.layer.sublayerTransform = CATransform3DMakeTranslation(15, 0, 0)

        
        navigationController?.navigationBar.barTintColor = UIColor.c2()
        
        let logo = UIImage(named: "LOGO")
        let imageView = UIImageView(image:logo)
        self.navigationItem.titleView = imageView
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    @IBAction func RegisterPressed(_ sender: Any) {
        //REGISTER
    }

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}

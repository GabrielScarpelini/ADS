package com.gabrielsp.lmsappn

import android.content.Context
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import com.gabrielsp.lmsappn.databinding.FragmentSecondBinding
import com.gabrielsp.lmsappn.databinding.LoginBinding
import com.gabrielsp.lmsappn.DebugActivity as DebugActivity
class MainActivity : AppCompatActivity() {

    private val binding by lazy {
        FragmentSecondBinding.inflate(layoutInflater)
    }
    private val context: Context get() = this


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        setContentView(R.layout.login)
        setContentView(binding.root)
        binding.imageView.setImageResource(R.drawable.dawn)
        binding.txtViewLogin.text = "Login do Amanhecer!"
        binding.loginButton.setOnClickListener {
            onClickLogin()
        }
    }

    fun onClickLogin() {
        val valorUsuario = binding.txtUsuario.text.toString()
        val valorSenha = binding.txtPassword.text.toString()
        Toast.makeText(
            this,

            "User: $valorUsuario  Password: $valorSenha",
            Toast.LENGTH_LONG
        ).show()

    }
}
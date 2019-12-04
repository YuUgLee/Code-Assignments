using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DamageControl : MonoBehaviour
{
    [SerializeField] private float playerdashdamage;
    [SerializeField] private DamageEnemy damagee;
    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.CompareTag("Enemy"))
        {
            Damage();
        }
    }
    void Damage()
    {
        damagee.m_CurrentHealth -= playerdashdamage;
        this.gameObject.SetActive(false);
    }
    
}

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DamageEnemy : MonoBehaviour
{
    public string enemyName;
    [SerializeField]
    public float m_MaxHealth = 100;
    public float m_CurrentHealth;
    private void Awake()
    {
        m_CurrentHealth = m_MaxHealth;
    }

    public void Damage(float damage)
    {
        m_CurrentHealth -= damage;
        if (Deadenemy())
        {
            Destroy(gameObject);
        }
    }
    public bool Deadenemy() {return m_CurrentHealth <=0;}

}

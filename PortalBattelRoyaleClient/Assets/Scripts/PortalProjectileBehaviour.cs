using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PortalProjectileBehaviour : MonoBehaviour
{
    // Start is called before the first frame update
    public Vector2 direction = Vector2.right;
    public float speed = 1f;
    void Start()
    {
        
    }

    void FixedUpdate()
    {
        transform.position = new Vector3(
            transform.position.x + direction.normalized.x * speed,
            transform.position.y + direction.normalized.y * speed,
            0
        );
        
    }
}

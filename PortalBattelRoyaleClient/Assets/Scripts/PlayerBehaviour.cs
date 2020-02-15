using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerBehaviour : MonoBehaviour
{
    public float movementSpeed = 1f;
    public float jumpSpeed = 10f;
    public float maxSpeed = 5f;


    private Rigidbody2D rb;
    private GameObject gun;

    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
        gun = transform.GetChild(0).gameObject;
    }

    void FixedUpdate()
    {
        if (Input.GetKey("a")) {
            rb.AddForce(new Vector2(-movementSpeed, 0));
        } else if (Input.GetKey("d")) {
            rb.AddForce(new Vector2(movementSpeed, 0));
        }

        if (Input.GetKeyDown("space")) {
            rb.AddForce(new Vector2(0, jumpSpeed));
        }

        rb.velocity = new Vector2(
            Mathf.Min(Mathf.Abs(rb.velocity.x), maxSpeed) * (rb.velocity.x > 0 ? 1f : -1f),
            rb.velocity.y
        );

        Vector3 mouseWorldPoint = Camera.main.ScreenToWorldPoint(Input.mousePosition);

        Vector2 gunRotation = mouseWorldPoint - transform.position;
        gun.transform.eulerAngles = new Vector3(
            0,
            0,
            Vector2.SignedAngle(Vector2.up, gunRotation)
        );

    }
}

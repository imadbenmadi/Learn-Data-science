# **🔹 Triggers & Events**

## **1️⃣ Triggers (Automate Actions on Table Changes)**

Triggers **automate operations** when `INSERT`, `UPDATE`, or `DELETE` occurs.

### **🔹 AFTER INSERT (Auto-log new records)**

```sql
CREATE TRIGGER after_employee_insert
AFTER INSERT ON employees
FOR EACH ROW
INSERT INTO employee_log(employee_id, action) VALUES (NEW.id, 'Inserted');
```

👉 Every time an employee is inserted, a log is added.

---

### **🔹 BEFORE UPDATE (Ensure Salary Never Goes Negative)**

```sql
CREATE TRIGGER before_salary_update
BEFORE UPDATE ON employees
FOR EACH ROW
BEGIN
    IF NEW.salary < 0 THEN
        SET NEW.salary = 0;
    END IF;
END;
```

👉 Ensures salary **never becomes negative**.

---

### **🔹 AFTER DELETE (Archive Deleted Data)**

```sql
CREATE TRIGGER after_employee_delete
AFTER DELETE ON employees
FOR EACH ROW
INSERT INTO deleted_employees(id, name, department) VALUES (OLD.id, OLD.name, OLD.department);
```

👉 Moves deleted employees into an archive table.

---

## **2️⃣ Event Scheduling (Automating Tasks)**

Events allow **scheduled execution** of queries (like cron jobs in Linux).

💡 **Example: Deleting Old Logs Every Day**

```sql
CREATE EVENT delete_old_logs
ON SCHEDULE EVERY 1 DAY
DO
DELETE FROM logs WHERE created_at < NOW() - INTERVAL 30 DAY;
```

👉 Runs **every day** to delete logs older than 30 days.

---

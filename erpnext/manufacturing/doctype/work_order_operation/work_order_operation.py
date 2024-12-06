# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors and contributors
# For license information, please see license.txt


from frappe.model.document import Document


class WorkOrderOperation(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		actual_end_time: DF.Datetime | None
		actual_operating_cost: DF.Currency
		actual_operation_time: DF.Float
		actual_start_time: DF.Datetime | None
<<<<<<< HEAD
		batch_size: DF.Float
		bom: DF.Link | None
		completed_qty: DF.Float
		description: DF.TextEditor | None
		hour_rate: DF.Float
=======
		backflush_from_wip_warehouse: DF.Check
		batch_size: DF.Float
		bom: DF.Link | None
		bom_no: DF.Link | None
		completed_qty: DF.Float
		description: DF.TextEditor | None
		fg_warehouse: DF.Link | None
		finished_good: DF.Link | None
		hour_rate: DF.Float
		is_subcontracted: DF.Check
>>>>>>> 125a352bc2 (fix: allow all dispatch address for drop ship invoice)
		operation: DF.Link
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		planned_end_time: DF.Datetime | None
		planned_operating_cost: DF.Currency
		planned_start_time: DF.Datetime | None
		process_loss_qty: DF.Float
		sequence_id: DF.Int
<<<<<<< HEAD
		status: DF.Literal["Pending", "Work in Progress", "Completed"]
		time_in_mins: DF.Float
=======
		skip_material_transfer: DF.Check
		source_warehouse: DF.Link | None
		status: DF.Literal["Pending", "Work in Progress", "Completed"]
		time_in_mins: DF.Float
		wip_warehouse: DF.Link | None
>>>>>>> 125a352bc2 (fix: allow all dispatch address for drop ship invoice)
		workstation: DF.Link | None
		workstation_type: DF.Link | None
	# end: auto-generated types

	pass
